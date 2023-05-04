from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(name, batch_code, submission_date, submitted_to):
    c = canvas.Canvas("report.pdf", pagesize=letter)
    c.drawString(50, 750, f"Name: {name}")
    c.drawString(50, 730, f"Batch Code: {batch_code}")
    c.drawString(50, 710, f"Submission Date: {submission_date}")
    c.drawString(50, 690, f"Submitted To: {submitted_to}")
    
    # Add snapshots of each step of deployment
    # Use c.drawImage("path/to/snapshot.png", x, y, width, height) to add images

    c.save()

generate_report("Your Name", "Batch Code", "Submission Date", "Submitted To")
