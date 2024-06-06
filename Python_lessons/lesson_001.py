
"""Exercice
Un magasin vend trois types de produits : des stylos, des cahiers et des calculatrices. Voici les informations concernant ces produits :

Stylos :

Prix d'achat : 1,20 €
Prix de vente : 2,00 €
Quantité achetée : 150

Cahiers :

Prix d'achat : 2,50 €
Prix de vente : 4,00 €
Quantité achetée : 100

Calculatrices :

Prix d'achat : 15,00 €
Prix de vente : 25,00 €
Quantité achetée : 30


Questions

1. Calcule le coût total d'achat pour chaque type de produit.
2. Calcule le revenu total de la vente pour chaque type de produit.
3. Calcule le bénéfice pour chaque type de produit.
4. Calcule le bénéfice total pour tous les produits.
5. Si le bénéfice total est partagé également entre 5 employés, combien chaque employé recevra-t-il ?
6. Quelle est la différence (modulo) entre le nombre total de stylos et le nombre total de cahiers ?
7. Si le prix d'achat des stylos augmente de 20%, quel sera le nouveau prix d'achat ?
8. Si le prix de vente des calculatrices double, quel sera le nouveau prix de vente ?
"""

# Declaration des variables
produit_1="stylo"
prix_dachat_stylo=1.2
prix_de_vente_stylo=2
quantite_stylo=150
#type de la variable

type(prix_dachat_stylo)
cout_total_stylo=prix_dachat_stylo*quantite_stylo
print(cout_total_stylo)
print("Le cout total des stylos est :", cout_total_stylo)
print(f"Le cout total des stylos est : {cout_total_stylo}")

# Le revenu est egal au prix de vente fois la quantite de stylo
revenu_total_stylo=prix_de_vente_stylo*quantite_stylo
print(f"Le revenu total des stylos est : {revenu_total_stylo}")
50-30 #soustraction
20/2 #division
3%2 #modulo
3**2 #root square