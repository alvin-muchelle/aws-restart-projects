import sys

# Store the human preproinsulin sequence in a variable called preproinsulin:

preproInsulin = sys.argv[1]

# Store the remaining sequence elements of human insulin in variables:

isInsulin =  sys.argv[2]
bInsulin =  sys.argv[3]
aInsulin =  sys.argv[4]
cInsulin = sys.argv[5]

insulin = sys.argv[6]

print(f"""preproInsulin: {preproInsulin}
isInsulin: {isInsulin}
bInsulin: {bInsulin}
cInsulin: {cInsulin}
aInsulin: {aInsulin}
insulin: {insulin}""")

# Dictionary of amino acid molecular weights
aaWeights = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
    'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
    'V': 117.15, 'W': 204.23, 'Y': 181.19
}

# Count the occurrences of each amino acid in insulin
aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights}
print(aaCountInsulin)

# Calculate molecular weight by summing (count * weight) for each amino acid
molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaCountInsulin)

# Print the molecular weight of insulin
print(f"The rough molecular weight of insulin: {molecularWeightInsulin:.2f} Da")

actualMolecularWeightInsulin = 5807.63
errorPercentage =((molecularWeightInsulin - actualMolecularWeightInsulin)/actualMolecularWeightInsulin)*100
print(f"Error Percentage: {errorPercentage:.2f}")