# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 360 (printed ٣٥٩)."""

PAGE_NUMBER = 360
PRINTED_PAGE = "٣٥٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(والثالث) أي: الضمير المجرور (متصل) فقط؛» from the foot of PDF p. 359.
    {"type": "matn",
     "ar": "لأنه لا مانع[[١]] فيه من الاتصال الذي هو الأصل، وستعرف المانع من الاتصال إن شاء الله تعالى",
     "en": "…because there is nothing in it preventing attachment, which is the default; you will come to know what prevents attachment, if Allah the Exalted wills."},
    {"type": "matn",
     "ar": "(فذلك) أي: المضمر (خمسة أنواع) المرفوع المتصل والمنفصل، والمنصوب المتصل والمنفصل، والمجرور المتصل.",
     "en": "(So that), that is, the pronoun, (is of five types): the nominative attached and detached, the accusative attached and detached, and the genitive attached."},
    {"type": "matn",
     "ar": "النوع (الأول) يعني: المرفوع المتصل ضمير (ضربت) على صيغة المتكلم الواحد المعلوم الماضي",
     "en": "(The first) type, namely the attached nominative, is the pronoun of (ḍarabtu) (I struck), in the form of the first person singular, active, past,"},
    {"type": "matn",
     "ar": "(وضربت) على صيغة المتكلم الواحد المجهول الماضي المنتهيين أولهما[[٢]] (إلى ضربن) على صيغة جمع الغائبة المعلوم الماضي",
     "en": "(and ḍuribtu) (I was struck), in the form of the first person singular, passive, past — the two of which end, the first of them, (at ḍarabna) (they [f.] struck), in the form of the third person feminine plural, active, past,"},
    {"type": "matn",
     "ar": "(و) ثانيهما إلى (ضربن) على صيغة جمع الغائبة المجهول الماضي.",
     "en": "(and) the second of them at (ḍuribna) (they [f.] were struck), in the form of the third person feminine plural, passive, past."},
    {"type": "matn",
     "ar": "وإنما بدأ بالمتكلم[[٣]]؛ لأن ضمير المتكلم أعرف المعارف[[٤]]، وأخر ضمير الغائب؛ لأنه دون الكل،",
     "en": "He began with the first person only because the first-person pronoun is the most definite of definites, and he put the third-person pronoun last because it ranks below all the others."},
    {"type": "matn",
     "ar": "وصورة التصريف هكذا: «ضربت، ضربنا، ضربت، ضربتما، ضربتم، ضربت، ضربتما، ضربتن، ضرب، ضربا، ضربوا، ضربت، ضربتا، ضربن» وعلى هذا القياس المجهول.",
     "en": "The paradigm runs thus: “ḍarabtu, ḍarabnā, ḍarabta, ḍarabtumā, ḍarabtum, ḍarabti, ḍarabtumā, ḍarabtunna, ḍaraba, ḍarabā, ḍarabū, ḍarabat, ḍarabatā, ḍarabna”; the passive follows the same pattern."},
    {"type": "matn",
     "ar": "(و) النوع (الثاني) أي: المرفوع المنفصل («أنا» إلى «هن») «أنا، نحن، أنت، أنتما، أنتم، أنت، أنتما، أنتن، هو، هما، هم، هي، هما، هن».",
     "en": "(And the second) type, that is, the detached nominative, is (from “anā” to “hunna”): “anā, naḥnu, anta, antumā, antum, anti, antumā, antunna, huwa, humā, hum, hiya, humā, hunna”."},
    {"type": "matn",
     "ar": "والضمير في «أنت» إلى «أنتن» هو «أن» إجماعا[[٥]]، والحروف الأواخر لواحق دالة على أحواله من الإفراد والتثنية والجمع والتذكير والتأنيث.",
     "en": "The pronoun in “anta” through “antunna” is “an” by consensus, and the final letters are suffixes indicating its states of singular, dual and plural, masculine and feminine."},
    {"type": "matn",
     "ar": "(و) النوع (الثالث) أي: المنصوب المتصل، وهو قسمان:",
     "en": "(And the third) type, that is, the attached accusative, is of two kinds:"},
    {"type": "matn",
     "ar": "القسم الأول: المتصل بالفعل نحو («ضربني» إلى «ضربهن») «ضربني، ضربنا، ضربك، ضربكما، ضربكم، ضربك، ضربكما، ضربكن، ضربه، ضربهما، ضربهم، ضربها، ضربهما، ضربهن».",
     "en": "The first kind is the one attached to the verb, as in (from “ḍarabanī” to “ḍarabahunna”): “ḍarabanī, ḍarabanā, ḍarabaka, ḍarabakumā, ḍarabakum, ḍarabaki, ḍarabakumā, ḍarabakunna, ḍarabahu, ḍarabahumā, ḍarabahum, ḍarabahā, ḍarabahumā, ḍarabahunna”."},
    # REVIEW: the first form is printed «إننه» (one would expect «إنني»); the list also lacks the
    # third-person forms between «إنه» and «إنهن». Transcribed as printed.
    {"type": "matn",
     "ar": "والقسم الثاني: المتصل بغير الفعل نحو: («إننه» إننا، إنك، إنكما، إنكم، إنك، إنكما، إنكن إنه (إلى «إنهن»)).",
     "en": "The second kind is the one attached to something other than the verb, as in: (“innanahu”, innanā, innaka, innakumā, innakum, innaki, innakumā, innakunna, innahu, (to “innahunna”))."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إن قلت: من الموانع الفصل، وقد يقع بين المضاف والمضاف إليه؟",
     "en": "If you say: separation is one of the preventing factors, and it may occur between the annexed noun and the noun annexed to it?"},
    {"type": "pair",
     "ar": "قلنا: لا يقع إذا كان المضاف إليه ضميرا مع أن الفصل بينهما مطلقا قبيح.",
     "en": "We say: it does not occur when the noun annexed to is a pronoun; moreover, separation between them is unseemly in all cases."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بدل من المستتر في المنتهيين بدل البعض من الكل،",
     "en": "[“Awwaluhumā”] is a substitute (badal) for the concealed pronoun in “al-muntahiyayn”, a substitution of part for whole."},
    {"type": "pair",
     "ar": "وأشار به إلى أن كلمة «إلى» للإسقاط لا لمد الحكم، فلا يلزم عدم دخول ما بعدها في الحكم.",
     "en": "By it he indicated that the word “ilā” is for dropping [the intermediate items], not for extending the ruling; so it does not follow that what comes after it is excluded from the ruling."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "والصرفيون يبدؤون بالغائب لتجرده عن اللواحق، ثم يراعون أسلوب الترقي.",
     "en": "The morphologists begin with the third person because it is free of suffixes, and then follow the method of ascending order."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ثم الأعرف من ضميري المتكلم الواحد.",
     "en": "Then [the more definite] of the two first-person pronouns is the singular."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "هكذا ذكره اللباب.",
     "en": "Thus did al-Lubāb state it."},
    {"type": "pair",
     "ar": "وقال شارحه العباب: أي إجماعا من البصريين، وإلا فالفراء جعل الضمير «أنت» بكماله وباقي الكوفيين ذهبوا إلى أنه التاء بتصاريفه.",
     "en": "Its commentator, al-ʿUbāb, said: that is, by consensus of the Baṣrans; otherwise al-Farrāʾ made the pronoun the whole of “anta”, and the rest of the Kūfans held that it is the tāʾ with its inflected forms."},
]
