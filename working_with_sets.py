beth_countries = ['Bulgaria', 'Israel', 'UK', 'Mexico', 'China', 'Uzbekistan',
    'Croatia', 'Tibet', 'Niger', 'Burkina Faso']

steve_countries = ['Israel', 'UK', 'China', 'Tibet', 'Austria', 'Cyprus',
        'Russia', 'Vietnam']

beth = set(beth_countries)
steve = set(steve_countries)

print("Both:", beth & steve)  # intersection
print("Only one:", beth ^ steve)  # Xor
print("Either:", beth | steve)  # union
print("Just Beth:", beth - steve)
print("Just Steve:", steve - beth)
