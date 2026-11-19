# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 352 (printed ٣٥١)."""

PAGE_NUMBER = 352
PRINTED_PAGE = "٣٥١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(وإذا كان) البدل (نكرة) مبدلة (من معرفة فالنعت) أي: نعت البدل النكرة» at the foot of PDF p. 351.
    {"type": "matn",
     "ar": "واجب[[١]] لئلا يكون المقصود أنقص من غير المقصود من كل وجه،",
     "en": "…is obligatory, so that what is intended is not inferior in every respect to what is not intended."},
    {"type": "matn",
     "ar": "فأتوا فيه بصفة حتى تكون كالجابر لما فيه من نقص النكارة (مثل: ﴿بالناصية ناصية كاذبة﴾[[٢]]).",
     "en": "So they brought an adjective with it, to act as a kind of compensation for the deficiency of indefiniteness in it, (as in “by the forelock, a lying forelock”)."},
    {"type": "matn",
     "ar": "(ويكونان ظاهرين) نحو: «جاءني زيد أخوك» (ومضمرين) نحو: «الزيدون لقيتهم إياهم» (ومختلفين) نحو: «أخوك ضربته زيدا»، و«أخوك ضربت زيدا إياه».",
     "en": "(They may be two explicit nouns), as in “jāʾanī Zaydun akhūka” (Zayd, your brother, came to me), (two pronouns), as in “al-Zaydūna laqītuhum iyyāhum” (the Zayds, I met them, them), (and differing), as in “akhūka ḍarabtuhu Zaydan” (your brother, I struck him, Zayd) and “akhūka ḍarabtu Zaydan iyyāhu” (your brother, I struck Zayd, him)."},
    {"type": "matn",
     "ar": "(ولا يبدل ظاهر من مضمر بدل الكل إلا من الغائب، نحو: «ضربته زيدا»)؛",
     "en": "(An explicit noun is not substituted for a pronoun as a substitute of the whole except for the third-person pronoun, as in “ḍarabtuhu Zaydan” [I struck him, Zayd]),"},
    {"type": "matn",
     "ar": "لأن المضمر المتكلم والمخاطب[[٣]] أقوى وأخص دلالة من الظاهر،",
     "en": "because the first- and second-person pronoun is stronger and more specific in signification than the explicit noun;"},
    {"type": "matn",
     "ar": "فلو أبدل الظاهر منهما بدل الكل يلزم أن يكون المقصود أنقص من غير المقصود مع كون مدلوليهما واحدا[[٤]]،",
     "en": "so were the explicit noun substituted for them as a substitute of the whole, it would follow that what is intended is inferior to what is not intended, while what the two signify is one and the same,"},
    {"type": "matn",
     "ar": "بخلاف بدل البعض والاشتمال والغلط؛ فإن المانع فيها مفقود[[٥]]؛ إذ ليس مدلول الثاني فيها مدلول الأول،",
     "en": "unlike the substitute of the part, of inclusion and of error, for in these the impediment is absent, since in them what the second signifies is not what the first signifies."},
    {"type": "matn",
     "ar": "فيقال: «اشتريتك نصفك، واشتريتني نصفي، وأعجبتني علمك، وأعجبتك علمي، وضربتك الحمار، وضربتني الحمار».",
     "en": "So one says: “ishtaraytuka niṣfaka” (I bought you, half of you), “ishtaraytanī niṣfī” (you bought me, half of me), “aʿjabtanī ʿilmuka” (you pleased me, your knowledge), “aʿjabtuka ʿilmī” (I pleased you, my knowledge), “ḍarabtuka al-ḥimāra” (I struck you—the donkey) and “ḍarabtanī al-ḥimāra” (you struck me—the donkey)."},

    {"type": "section", "ar": "[عطف البيان]",
     "en": "The Explicative Apposition (ʿAṭf al-Bayān)"},

    {"type": "matn",
     "ar": "(عطف البيان: تابع) شامل جميع التوابع (غير صفة) احترز به عن الصفة",
     "en": "(The explicative apposition is a follower), which covers all the followers (tawābiʿ), (other than an adjective): by this he excludes the adjective,"},
    {"type": "matn",
     "ar": "(يوضح متبوعه) احترز به عن البدل والعطف بالحرف والتأكيد،",
     "en": "(that clarifies its antecedent): by this he excludes the substitute, conjunction by a particle, and corroboration (taʾkīd)."},
    {"type": "matn",
     "ar": "ولا يلزم من ذلك أن يكون عطف البيان أوضح من متبوعه، بل ينبغي أن يحصل من اجتماعهما إيضاح لم يحصل من أحدهما على الانفراد، فيصح أن يكون الأول أوضح من الثاني",
     "en": "It does not follow from this that the explicative apposition is clearer than its antecedent; rather, from the two together there should arise a clarification that does not arise from either alone, so it is sound for the first to be clearer than the second,"},
    {"type": "matn",
     "ar": "(مثل:",
     "en": "(as in:"},
    {"type": "verse",
     "ar": "«أقسم بالله أبو حفص عمر»)",
     "en": "“Abū Ḥafṣ ʿUmar swore by Allah”)."},
    {"type": "matn",
     "ar": "فـ«أبو حفص» كنية عمر بن الخطاب رضي الله تعالى عنه، و«عمر» عطف بيان له.",
     "en": "“Abū Ḥafṣ” is the kunya of ʿUmar ibn al-Khaṭṭāb, may Allah the Exalted be pleased with him, and “ʿUmar” is an explicative apposition to it."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    # REVIEW: «فإنها المبدل منه» printed; the sense seems to call for something like «يفيدها المبدل منه»; transcribed as printed.
    {"type": "pair",
     "ar": "قال الشيخ الرضي: هذا ليس إلا في بدل الكل، بل عند أبي علي بدل الكل أيضا مقيد بما إذا لم يشتمل على فائدة، فإنها المبدل منه",
     "en": "Shaykh al-Raḍī said: this applies only to the substitute of the whole; indeed, according to Abū ʿAlī, the substitute of the whole too is restricted to the case where it does not contain a benefit, for that is [what] the substituted-for [provides],"},
    {"type": "pair",
     "ar": "نحو قوله تعالى: ﴿بالواد المقدس طوى﴾ (سورة طه: ١٢) أي: مقدس مرتين.",
     "en": "as in His words, Exalted is He, “in the sanctified valley, Ṭuwā” (Qurʾān, Sūrat Ṭāhā 20:12), that is, sanctified twice."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "سورة العلق: ١٥-١٦.",
     "en": "Qurʾān, Sūrat al-ʿAlaq 96:15–16."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيل: ولأنه يلزم أن يكون شيء غائبا ومخاطبا ومتكلما.",
     "en": "It has been said: and because it would follow that one thing is absent, addressed and speaking [at once]."},
    {"type": "pair",
     "ar": "وفيه بحث إذ يلزم منه ألا يجوز إبدال هذين الضميرين من الاسم الظاهر.",
     "en": "This is open to discussion, since it would follow from it that these two pronouns may not be substituted for an explicit noun."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "فلا يفيد زيادة على ما يفيده المبدل منه.",
     "en": "So it conveys nothing beyond what the substituted-for conveys."},
    {"type": "pair",
     "ar": "وفيه أن المفهومين متغايران. غاية ما في الباب أنهما متحدان بحسب الذات.",
     "en": "Against this: the two concepts are distinct; the most that can be said is that they are one in essence."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فيفيد ما لا يفيده المبدل منه.",
     "en": "So it conveys what the substituted-for does not convey."},
]
