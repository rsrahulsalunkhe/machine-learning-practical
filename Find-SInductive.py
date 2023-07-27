#Implement the Find-S Inductive Learning algorithm.

def initilize_hypothesis(attributs):
    return ["0"] * len(attributs)

def find_s_algo(training_data):
    attributs = trainig_data[0][:-1]
    hypothesis = initilize_hypothesis(attributs)
    
    for i in trainig_data:
        x, y = i[:-1], i[-1]

        if y == "Y":
            for j in range(len(attributs)):
                if hypothesis[j] == "0":
                    hypothesis[j] = x[j]
                elif hypothesis[j] != x[j]:
                    hypothesis[j] = "?"

    return hypothesis
        

trainig_data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Y"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Y"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "N"],
    ["Sunny", "Warm", "Normal", "Strong", "Cood", "Change", "Y"]
]

hypothesis = find_s_algo(trainig_data)
print("Final Hypothesis", hypothesis)
