# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 600 (printed ٥٩٩) — end of the work and colophon."""

PAGE_NUMBER = 600
PRINTED_PAGE = "٥٩٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the closing prayer «… في محو أرقام الضلالات كافية، وعن» at the foot of PDF p. 599.
    {"type": "matn",
     "ar": "مضرة إسقام الجهالات شافية، وعلى آله وأصحابه وعلى من تبعهم من زمرة أحبابه.",
     "en": "…the harm of the sicknesses of ignorance healing; and upon his family and his companions, and upon those of the company of his beloved ones who followed them."},

    # ---------------- Colophon (no heading printed) ----------------
    # REVIEW: «مكد الانتهاض» is clearly printed; «مكد» is read as the place of toil (from كد); rendered accordingly.
    {"type": "matn",
     "ar": "وقد استراح من مكد الانتهاض، لنقل هذا الشرح من السواد إلى البياض، العبد الفقير عبد الرحمن الجامي",
     "en": "The poor servant ʿAbd al-Raḥmān al-Jāmī rested from the toil of rising to transfer this commentary from the draft (sawād) to the fair copy (bayāḍ)"},
    {"type": "matn",
     "ar": "-وفقه الله سبحانه وتعالى وظائف عبوديته للإعراض عن مطالبة الأعواض والأغراض-",
     "en": "— may Allah, Glorified and Exalted is He, grant him success in the duties of his servanthood, so as to turn away from seeking recompense and personal ends —"},
    {"type": "matn",
     "ar": "ضحوة السبت الحادي عشر من رمضان المعظم في سلك شهور سنة سبع وتسعين وثمانمائة من الهجرة النبوية،",
     "en": "in the forenoon of Saturday, the eleventh of the venerated Ramaḍān, in the string of the months of the year eight hundred and ninety-seven of the Prophetic Hijra."},
    {"type": "matn",
     "ar": "والحمد لله رب العالمين، والصلاة والسلام على محمد وآله أجمعين.",
     "en": "Praise belongs to Allah, Lord of the worlds, and blessings and peace be upon Muḥammad and all his family."},
]
