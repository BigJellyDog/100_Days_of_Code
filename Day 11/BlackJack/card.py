# def card_art_drawing(cards):
#     """Prints multiple cards with varying ranks and suits."""
#     card_art = [
#         ("┌─────────────┐",
#          "│ {0}           │",
#          "│             │",
#          "│             │",
#          "│      {1} \u2002    │",
#          "│             │",
#          "│             │",
#          "│           {0} │",
#          "└─────────────┘")
#     ]
#
#     fixed_width_space = '\u2002'
#     for i in range(9):
#         for rank, suit in cards:
#             current_card = [line.format(rank, suit) for line in card_art[0]]
#             print(current_card[i], end="  ")
#
#         print("")

phand = ["2 of ♥", "K of ♦", "A of ♣"]


def mk_card(s):
  pcarddisplay = []
  pcarddisplay.append("┌─────────────┐")
  pcarddisplay.append("│ {}           │")
  pcarddisplay.append("│             │")
  pcarddisplay.append("│             │")
  pcarddisplay.append("│     {0}     │")
  pcarddisplay.append("│             │")
  pcarddisplay.append("│             │")
  pcarddisplay.append("│           {} │")
  pcarddisplay.append("└─────────────┘")

  x = ("│ ", s[:1], "           │")
  pcarddisplay[1] = "".join(x)

  x = ("│           ", s[:1], " │")
  pcarddisplay[7] = "".join(x)

  if "♦" in s:
    pcarddisplay[4] = "│      ♦\u2002     │"
  if "♣" in s:
    pcarddisplay[4] = "│      ♣\u2002     │"
  if "♥" in s:
    pcarddisplay[4] = "│      ♥\u2002     │"
  if "♠" in s:
    pcarddisplay[4] = "│      ♠\u2002     │"

  return pcarddisplay


print('\n'.join(map('  '.join, zip(*(mk_card(c) for c in phand)))))

