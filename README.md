# Loan Amortisation Calculator (Python)

A Python-based financial modelling tool that simulates loan repayment structures using amortisation principles. The system calculates monthly repayments, interest breakdowns, and generates structured repayment schedules for financial analysis and learning purposes.

---

## Project Overview

This project is a command-line loan amortisation calculator that allows users to input loan details and receive calculated outputs such as monthly repayments and full repayment schedules.

It demonstrates applied knowledge of financial mathematics, algorithm design, and Python programming for fintech-style problem solving.

---

## Features

- Monthly loan repayment calculation using amortisation formula  
- Monthly interest rate calculation  
- Full loan repayment schedule generation  
- Principal vs interest breakdown per month  
- Input validation for user-friendly interaction  
- Structured output using pandas DataFrame  

---

## Tech Stack

- Python 3  
- Pandas  
- NumPy  
- Math library  

---

## Financial Logic

- Monthly interest rate = annual interest / 12  
- Monthly payment calculated using the standard amortisation formula  
- Each payment is split into:
  - Interest portion  
  - Principal repayment  
- The remaining balance is updated each month  

---

## Example Output

| Month | Payment | Interest Paid | Principal Paid | Remaining Balance |
|------|--------|--------------|---------------|-------------------|
| 1 | R2,450.00 | R850.00 | R1,600.00 | R98,400.00 |
| 2 | R2,450.00 | R840.00 | R1,610.00 | R96,790.00 |

---

## How to Run

### 1. Clone the repository
git clone https://github.com/your-username/loan-amortisation-calculator.git

### 2. Move into project folder
cd loan-amortisation-calculator

### 3. Install dependencies
pip install pandas numpy

### 4. Run the program
python loan_amortisation_calculator.py

---

## Project Structure
loan-amortisation-calculator/
│
├── loan_amortisation_calculator.py
├── README.md


---

## Future Improvements

- Web-based interface (Flask or Streamlit)
- Export schedule to PDF or Excel
- Graphical visualisation of repayment trends
- Loan history storage using a database
- Interest rate input flexibility

---

## Author

Thamsanqa Ngutshana  
Focused on Python development, financial modelling, and fintech applications.

---

## Notes

This project was developed for learning purposes to demonstrate financial computation, algorithm design, and Python-based problem solving.
