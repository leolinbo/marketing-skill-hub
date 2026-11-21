$excel = New-Object -ComObject Excel.Application
$excel.Visible = $false
try {
    $filePath = 'C:\Users\HUAWEI\Desktop\ENCORE社媒客户清单 V0 20261023张林波.xlsx'
    $wb = $excel.Workbooks.Open($filePath)
    $ws = $wb.Sheets.Item(1)
    
    # 查找第一行空行（从第5行开始，看A列）
    $row = 5
    while ($ws.Cells.Item($row, 3).Text -ne "" -or $ws.Cells.Item($row, 1).Text -ne "") {
        $row++
    }
    
    $no = $row - 4
    Write-Output "Inserting into row: $row with NO: $no"
    
    # A4: NO#
    # B4: Date
    # C4: Company/Personal Name
    # D4: Website
    # E4: Country
    # F4: 客户背调
    # G4: 是否匹配
    # H4: 客户类型
    # I4: 客户等级
    # J4: Contact Person
    # K4: Contact No. WhatsApp
    # L4: Contact No. Email
    # M4: Customer Business Scope
    # N4: Products Needed
    # O4: Follow issue
    # P4: 跟进人
    # Q4: 是否成交
    # R4: 是否互动上
    # S4: 最新动态
    # T4: Remark

    $todayStr = (Get-Date).ToString("yyyy/MM/dd")
    $ws.Cells.Item($row, 1).Value2 = $no
    $ws.Cells.Item($row, 2).Value2 = $todayStr
    $ws.Cells.Item($row, 3).Value2 = "Beki Tobiasson (Beki Tobiasson Art)"
    $ws.Cells.Item($row, 4).Value2 = "https://bekitobiassonartist.com"
    $ws.Cells.Item($row, 5).Value2 = "美国 (犹他州)"
    $ws.Cells.Item($row, 6).Value2 = "美国当代知名油画家（写实/具象/花卉），作品参展春维尔艺术博物馆等主流展馆；拥有10x12英尺私人油画画室，要求5000K色温、95+ CRI顶级显色照明用于专业画室油画调色"
    $ws.Cells.Item($row, 7).Value2 = "是"
    $ws.Cells.Item($row, 8).Value2 = "终端艺术工作室/画家主理人"
    $ws.Cells.Item($row, 9).Value2 = "A (高意向专业买家)"
    $ws.Cells.Item($row, 10).Value2 = "Beki Tobiasson"
    $ws.Cells.Item($row, 11).Value2 = "+1 801-358-6625"
    $ws.Cells.Item($row, 12).Value2 = "bekitobiasson@gmail.com"
    $ws.Cells.Item($row, 13).Value2 = "油画艺术创作与展览、艺术工作室运营"
    $ws.Cells.Item($row, 14).Value2 = "画室专业照明：5000K、CRI 95+ 高显色防眩光轨道灯/洗墙灯或筒灯，适配10x12英尺油画工作室"
    $ws.Cells.Item($row, 15).Value2 = "Shopify(encorebeam.com)表单直接询盘，询问10x12画室需配置几盏灯。业务员需提供照度方案、询问层高与轨道/筒灯偏好，加WhatsApp推进"
    $ws.Cells.Item($row, 16).Value2 = "待分配"
    $ws.Cells.Item($row, 17).Value2 = "否"
    $ws.Cells.Item($row, 18).Value2 = "待跟进"
    $ws.Cells.Item($row, 19).Value2 = "官网独立站询盘直达，已完成全网深度艺术背景背调"
    $ws.Cells.Item($row, 20).Value2 = "表单ID: ContactForm-AVFJHdFhzSVdoYTBIN__contact_form_dJqVC7；归属encorebeam.com零售站"
    
    $wb.Save()
    $wb.Close($true)
    Write-Output "SUCCESS: Saved inquiry to Excel successfully."
} catch {
    Write-Error $_
} finally {
    $excel.Quit()
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($excel) | Out-Null
}
