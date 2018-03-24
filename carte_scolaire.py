import argparse

STREET_PROPOSAL = "https://citoyens.ville-nice.fr/maelis-educ/shared/ajax/streetProposal.dhtml?item={search}&type=undefined"

parser = argparse.ArgumentParser(description='Recherche l´école maternelle associée à une adresse')
parser.add_argument("-n", "--numero", help="Numéro de rue", type=int)
parser.add_argument("-b", "--bis", help="Est un bis, ter, quater?", choices=["bis", "ter", "quater"])
parser.add_argument("-r", "rue", help="Rue")

args = parser.parse_args()

