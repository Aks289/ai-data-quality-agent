def generate_insights(df):

    insights = []

    missing_total = df.isnull().sum().sum()

    if missing_total == 0:
        insights.append(
            "Dataset contains no missing values."
        )

    else:
        insights.append(
            f"Dataset contains {missing_total} missing values."
        )

    duplicates = df.duplicated().sum()

    if duplicates > 0:

        insights.append(
            f"{duplicates} duplicate records detected."
        )

    else:

        insights.append(
            "No duplicate records detected."
        )

    return insights