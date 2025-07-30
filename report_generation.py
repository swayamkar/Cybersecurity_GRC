import pandas as pd
import matplotlib.pyplot as plt  # For visualizations

def generate_compliance_report(control_mapping, framework):
    # Create report structure and content
    report = f"Compliance Report for {config.FRAMEWORK_NAME}\n\n"
    # ...
    # Generate visualizations
    compliance_status_counts = control_mapping.value_counts()
    plt.bar(compliance_status_counts.index, compliance_status_counts.values)
    plt.xlabel("Compliance Status")
    plt.ylabel("Number of Controls")
    plt.title("Compliance Overview")
    plt.savefig("reports/compliance_overview.png")
    # ...
    return report
