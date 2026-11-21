# PowerShell script to validate skills
$skills = Get-ChildItem -Directory -Path (Join-Path $PSScriptRoot "..\skills")
$fail = 0

foreach ($dir in $skills) {
    $s = $dir.Name
    $dirFail = 0
    $f = Join-Path $dir.FullName "SKILL.md"
    if (-not (Test-Path $f)) {
        Write-Host "✗ ${s}: missing SKILL.md" -ForegroundColor Red
        $fail = 1
        continue
    }
    $content = Get-Content $f -Raw
    if (-not ($content -match "^---`r?`n")) {
        Write-Host "✗ ${s}: missing frontmatter" -ForegroundColor Red
        $dirFail = 1
    }
    if ($content -match '(?m)^name:\s*([a-z0-9-]+)') {
        $name = $matches[1]
        if ($name -ne $s) {
            Write-Host "✗ ${s}: name '$name' does not match folder" -ForegroundColor Red
            $dirFail = 1
        }
    } else {
        Write-Host "✗ ${s}: name not found" -ForegroundColor Red
        $dirFail = 1
    }
    if (-not ($content -match '(?m)^description:\s*.{40,}')) {
        Write-Host "✗ ${s}: description missing or too short" -ForegroundColor Red
        $dirFail = 1
    }
    $zh = Join-Path $dir.FullName "SKILL.zh.md"
    if (-not (Test-Path $zh)) {
        Write-Host "✗ ${s}: missing SKILL.zh.md" -ForegroundColor Red
        $dirFail = 1
    }
    # Check references
    $refs = [regex]::Matches($content, 'references/[a-z0-9-]+\.md') | ForEach-Object { $_.Value } | Select-Object -Unique
    foreach ($r in $refs) {
        $refPath = Join-Path $dir.FullName $r
        # Try local skill dir first, then look across skills/*
        if (-not (Test-Path $refPath)) {
            $globalRef = Get-ChildItem -Path (Join-Path $PSScriptRoot "..\skills") -Recurse -Filter (Split-Path $r -Leaf) -ErrorAction SilentlyContinue | Select-Object -First 1
            if (-not $globalRef) {
                Write-Host "✗ ${s}: broken link ${r}" -ForegroundColor Red
                $dirFail = 1
            }
        }
    }
    if ($dirFail -eq 0) {
        Write-Host "✓ ${s}" -ForegroundColor Green
    } else {
        $fail = 1
    }
}

if ($fail -eq 0) {
    Write-Host "`nAll skills validated successfully!" -ForegroundColor Green
} else {
    Write-Host "`nSome skills failed validation." -ForegroundColor Red
}
exit $fail
