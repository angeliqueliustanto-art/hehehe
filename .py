
import streamlit as st
import math

st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("Scientific Calculator")
st.write("A calculator for basic and advanced mathematical operations.")

st.divider()

st.subheader("Calculator")

operation = st.selectbox(
    "Select an operation:",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Square Root",
        "Logarithm (log base 10)",
        "Natural Logarithm (ln)",
        "Sine",
        "Cosine",
        "Tangent",
        "Factorial"
    ]
)

if operation in [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Power"
]:

    num1 = st.number_input(
        "Enter the first number:",
        value=0.0
    )

    num2 = st.number_input(
        "Enter the second number:",
        value=0.0
    )

else:

    num = st.number_input(
        "Enter a number:",
        value=0.0
    )

if st.button("Calculate", use_container_width=True):

    try:

        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        elif operation == "Division":

            if num2 == 0:
                st.error("Error: Cannot divide by zero.")
                st.stop()

            result = num1 / num2

        elif operation == "Power":
            result = num1 ** num2

        elif operation == "Square Root":

            if num < 0:
                st.error("Error: Cannot calculate the square root of a negative number.")
                st.stop()

            result = math.sqrt(num)

        elif operation == "Logarithm (log base 10)":

            if num <= 0:
                st.error("Error: Logarithm requires a positive number.")
                st.stop()

            result = math.log10(num)

        elif operation == "Natural Logarithm (ln)":

            if num <= 0:
                st.error("Error: Natural logarithm requires a positive number.")
                st.stop()

            result = math.log(num)

        elif operation == "Sine":
            result = math.sin(math.radians(num))

        elif operation == "Cosine":
            result = math.cos(math.radians(num))

        elif operation == "Tangent":

            if num % 180 == 90:
                st.error("Error: Tangent is undefined at this angle.")
                st.stop()

            result = math.tan(math.radians(num))

        elif operation == "Factorial":

            if num < 0 or not num.is_integer():
                st.error("Error: Factorial requires a non-negative integer.")
                st.stop()

            if num > 170:
                st.error("Error: Number is too large.")
                st.stop()

            result = math.factorial(int(num))

        st.success("Calculation completed!")

        st.subheader("Result")

        st.metric(
            label=operation,
            value=f"{result:.10g}"
        )

    except ValueError:
        st.error("Error: Please enter a valid number.")

    except OverflowError:
        st.error("Error: Calculation is out of range.")

    except ZeroDivisionError:
        st.error("Error: Cannot divide by zero.")

st.divider()

st.caption("Scientific Calculator | Built with Python and Streamlit")
