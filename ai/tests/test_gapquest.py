from gapquest.gapquest import GapQuest


def print_report_items(items):

    for item in items:

        print(f"- {item.text}")

        if item.evidence:

            print("  Evidence:")

            for evidence in item.evidence:

                print(
                    f"    • {evidence.paper_title}"
                    f"  ({evidence.section})"
                )

        print()


print("Starting GapQuest...\n")

gapquest = GapQuest()

print("\nClearing database...\n")

gapquest.vector_store.clear()

print("\nIngesting folder...\n")

gapquest.ingest_folder(
    "papers"
)

print("\nAsking GapQuest...\n")

report = gapquest.ask(
    "What are the research gaps in renewable energy?"
)

print("\n" + "=" * 80)
print("DOMAIN\n")
print(report.domain)

print("\n" + "=" * 80)
print("FOCUS AREA\n")
print(report.focus_area)

print("\n" + "=" * 80)
print("SUMMARY\n")
print(report.summary)

print("\n" + "=" * 80)
print("KEY FINDINGS\n")

print_report_items(report.key_findings)

print("\n" + "=" * 80)
print("COMMON THEMES\n")

print_report_items(report.common_themes)

print("\n" + "=" * 80)
print("CONTRADICTIONS\n")

if report.contradictions:
    print_report_items(report.contradictions)
else:
    print("No significant contradictions were identified across the analyzed literature.")

print("\n" + "=" * 80)
print("RESEARCH GAPS\n")

print_report_items(report.research_gaps)

print("\n" + "=" * 80)
print("FUTURE RECOMMENDATIONS\n")

print_report_items(report.future_recommendations)

print("\n" + "=" * 80)
print("CONFIDENCE\n")
print(report.confidence_score)