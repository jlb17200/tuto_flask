def get_users():
    return [
        {
            'first_name': "jl",
            'last_name': "bobo",
            'email': "<h1>toto@gmail.com</h1>"
        },
        {
            'first_name': "sonia",
            'last_name': "het",
            'email': "titi@gmail.com"
        },
        {
            'first_name': 'john',
            'last_name': 'doe',
            'email': "<script>alert('Je suis John et i l y a une faille XSS');</script>"
        }
    ]
