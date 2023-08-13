def domain_filter(file, searched_word, reasult_file):
    subdomains = []
    with open(file, 'r') as f:
        for line in f:
            domain = line.strip()
            if searched_word.lower() in domain.lower():
                subdomains.append(domain)

    with open(result_file, 'w') as f_out:
        for domain in subdomains:
            f_out.write(domain + '\n')


if __name__ == "__main__":
    domain_names = "domain_names.txt" 
    searched_word = "contact"
    result_file = "apple_results.txt"

    filtruj_domeny(domain_names, searched_word, result_file)

    print("The result saved in:", result_file)
