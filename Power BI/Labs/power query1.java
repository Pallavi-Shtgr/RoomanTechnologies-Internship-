// Tasks: 
// 1. Download and Prepare Data: • Download the Financial sample Excel workbook.
//     • Import the data into Power BI Desktop. 
//     • Perform necessary data transformations, such as changing data types and formatting. 
//  2. Develop Visuals: o Create a line chart to analyze profits over time. o Use a map visualization to display profit distribution by country/region. 
//  Construct a bar chart to evaluate sales by product and segment. 
//  3. Report Enhancement: Add a slicer to allow filtering by date. 
//  Apply the "Executive" theme to enhance the visual appeal of your report.

import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

public class FinancialReport {
    public static void main(String[] args) throws IOException {
        // Define file path of the Excel file
        String filePath = "financial_data.xlsx";
        
        // Create file input stream
        FileInputStream fis = new FileInputStream(new File(filePath));
        
        // Create workbook instance (for Excel 2007 and later versions)
        Workbook workbook = new XSSFWorkbook(fis);
        
        // Get the first sheet from the workbook
        Sheet sheet = workbook.getSheetAt(0);
        
        // Iterate over the rows and columns
        for (Row row : sheet) {
            // Assuming the first row is the header row
            if (row.getRowNum() == 0) continue;  // Skip header row
            
            // Get values from each column
            Cell dateCell = row.getCell(0);  // Example: Date column
            Cell profitCell = row.getCell(1); // Example: Profit column
            
            // Ensure the cells are not null and read values
            if (dateCell != null && profitCell != null) {
                String date = dateCell.toString();
                double profit = profitCell.getNumericCellValue();
                
                // Print out the row data
                System.out.println("Date: " + date + " | Profit: " + profit);
            }
        }
        
        workbook.close();
        fis.close();
    }
}
