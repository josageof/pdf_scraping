# PDF scraping using Tabula - Py

<span style="font-size:18px;">
To this day, do you still fetch data from PDFs using Ctrl+F? <br>
...and how do you do it when there are more than a <span style=" color:red;">hundred</span> files?
</span>

One way is to use the schema provided in scraping.py which reads the PDFs contained in user-defined
directories/subdirectories and lists the data tables found, based on keywords.
Finally, the tables are delivered as Sheets in a Excel file.

To install Tabula:
```
pip install tabula-py
```
Enjoy!