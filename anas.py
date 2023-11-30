def recommendation(domain):
    data = pickle.load(open('data.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    if domain not in data['Area_of_Interest_1'].values:
        return f"Domain '{domain}' not found in the dataset."

    domain_data = data[data['Area_of_Interest_1'] == domain]
    domain_indices = domain_data.index
    idx = domain_indices[0]
    similarity_scores = similarity[idx]
    similar_indices = np.argsort(similarity_scores)[::-1]

    recommended_employees = [
        {"Ename": data.loc[i, 'Ename']} for i in similar_indices[:20]
    ]

    return recommended_employees
