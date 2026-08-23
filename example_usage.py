from client import DifferentialPrivacySyntheticDataGeneratorClient

def main():
    client = DifferentialPrivacySyntheticDataGeneratorClient()
    res = client.generate_synthetic_dataset(record_count=5000, epsilon_budget=0.8)
    print('Records: ' + str(res['records_generated_count']) + ' | Fidelity: ' + str(res['statistical_fidelity_score']) + '% | PII Risk: ' + str(res['pii_leakage_risk_pct']) + '%')
    print('Compliance: ' + res['compliance_certification'])
    print('Sample Generated Records:')
    for s in res['sample_records']:
        print('  ' + str(s))

if __name__ == '__main__':
    main()
