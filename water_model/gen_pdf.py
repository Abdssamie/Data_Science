from fpdf import FPDF

# Adding EDA section with common code blocks for visualizations
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Data Science Project Workflow", ln=True, align='C')

# Section: Exploratory Data Analysis (EDA) with Code Blocks
pdf.ln(10)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Exploratory Data Analysis (EDA)", ln=True)

eda_intro = (
    "During Exploratory Data Analysis (EDA), you analyze the data through visualizations "
    "and statistical summaries. Visualizations such as histograms, box plots, and scatter "
    "plots can help uncover patterns, relationships, and trends in your data."
)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, eda_intro)

# Sub-section: Common EDA Code Blocks
pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Common Code Blocks for EDA", ln=True)

# Code for Statistical Summary
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Statistical Summary", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, 'df.describe()\n'
                      'df["column_name"].mean()\n'
                      'df["column_name"].median()\n'
                      'df["column_name"].std()')

# Code for Histogram
pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Histogram", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, 'import matplotlib.pyplot as plt\n\n'
                      '# Plot a histogram for a single column\n'
                      'df["column_name"].hist(bins=30)\n'
                      'plt.xlabel("Value")\n'
                      'plt.ylabel("Frequency")\n'
                      'plt.title("Histogram of column_name")\n'
                      'plt.show()')

# Code for Box Plot
pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Box Plot", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, 'import seaborn as sns\n\n'
                      '# Create a box plot\n'
                      'sns.boxplot(x="column_name", data=df)\n'
                      'plt.title("Box Plot of column_name")\n'
                      'plt.show()')

# Code for Scatter Plot
pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, txt="Scatter Plot", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 10, 'import matplotlib.pyplot as plt\n\n'
                      '# Create a scatter plot between two variables\n'
                      'plt.scatter(df["column_x"], df["column_y"])\n'
                      'plt.xlabel("Column X")\n'
                      'plt.ylabel("Column Y")\n'
                      'plt.title("Scatter Plot between column_x and column_y")\n'
                      'plt.show()')

# Save the updated PDF to a file
updated_file_name = r"C:\Users\abdss\Downloads\Data_Science_Project_Workflow.pdf"
pdf.output(updated_file_name)

updated_file_name
