# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 350 (printed ٣٤٩)."""

PAGE_NUMBER = 350
PRINTED_PAGE = "٣٤٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… فـ«زيد وأخوك» وإن اختلفا» at the foot of PDF p. 349.
    {"type": "matn",
     "ar": "مفهوما فهما متحدان ذاتا.",
     "en": "…in concept, they are one in essence."},
    {"type": "matn",
     "ar": "قال الشارح الرضي: وأنا إلى الآن لم يظهر لي فرق جلي بين بدل الكل من الكل وبين عطف البيان، بل لا أرى عطف البيان إلا بدل الكل[[١]]،",
     "en": "The commentator al-Raḍī said: “Up to now no clear difference has appeared to me between the substitute of the whole for the whole (badal al-kull min al-kull) and the explicative apposition (ʿaṭf al-bayān); indeed, I regard explicative apposition as nothing but the substitute of the whole.”"},
    {"type": "matn",
     "ar": "وما قالوا من أن الفرق بينهما أن البدل هو المقصود بالنسبة بدون متبوعه، بخلاف عطف البيان، فإنه بيان، والبيان فرع المبين[[٢]]، فيكون المقصود هو الأول.",
     "en": "As for what they said—that the difference between them is that the substitute (badal) is what is intended by the attribution without its antecedent, unlike the explicative apposition, for it is an explanation, and the explanation is subsidiary to what is explained, so that what is intended is the first—"},
    {"type": "matn",
     "ar": "فالجواب: أنا لا نسلم أن المقصود في بدل الكل هو الثاني فقط، ولا في سائر الأبدال إلا الغلط[[٣]].",
     "en": "the answer is that we do not grant that what is intended in the substitute of the whole is the second alone, nor in the other kinds of substitute, except the substitute of error (ghalaṭ)."},
    {"type": "matn",
     "ar": "وقال بعض المحققين في جوابه: الظاهر أنهم لم يريدوا أنه ليس مقصودا بالنسبة أصلا، بل أرادوا أنه ليس مقصودا أصليا.",
     "en": "One of the verifying scholars said in reply to him: what is apparent is that they did not mean that it [the first] is not intended by the attribution at all; rather, they meant that it is not the primary object of intent."},
    {"type": "matn",
     "ar": "والحاصل: أن مثل قولك: «جاءني أخوك زيد» إن قصدت فيه الإسناد إلى الأول، وجئت بالثاني تتمة له وتوضيحا، فالثاني عطف البيان،",
     "en": "The upshot is that in a phrase such as “jāʾanī akhūka Zaydun” (your brother Zayd came to me), if you intend the attribution to the first and bring the second as a completion and clarification of it, the second is an explicative apposition;"},
    {"type": "matn",
     "ar": "وإن قصدت فيه الإسناد إلى الثاني[[٤]] وجئت بالأول توطئة له ومبالغة في الإسناد فالثاني بدل،",
     "en": "and if you intend the attribution to the second and bring the first as a preparation for it and as emphasis in the attribution, the second is a substitute."},
    {"type": "matn",
     "ar": "وحينئذ يكون التوضيح الحاصل به مقصودا تبعا، والمقصود أصالة هو الإسناد إليه بعد التوطئة، فالفرق ظاهر.",
     "en": "In that case the clarification it yields is intended secondarily, while what is intended primarily is the attribution to it after the preparation. So the difference is evident."},
    {"type": "matn",
     "ar": "(والثاني) أي: بدل البعض (جزؤه) أي: جزء المبدل منه، نحو: «ضربت زيدا رأسه».",
     "en": "(And the second), that is, the substitute of the part (badal al-baʿḍ), (is a part of it), that is, a part of what is substituted for (al-mubdal minhu), as in “ḍarabtu Zaydan raʾsahu” (I struck Zayd, his head)."},
    {"type": "matn",
     "ar": "(والثالث) أي: بدل الاشتمال (بينه وبين الأول) أي: المبدل منه (ملابسة) بحيث توجب النسبة إلى المتبوع النسبة إلى الملابس إجمالا[[٥]]،",
     "en": "(And the third), that is, the substitute of inclusion (badal al-ishtimāl), (between it and the first), that is, what is substituted for, (there is a connection) (mulābasa), such that attribution to the antecedent entails, in a general way, attribution to what is connected with it,"},
    {"type": "matn",
     "ar": "نحو: «أعجبني زيد علمه» حيث يعلم ابتداء أنه يكون «زيد» معجبا باعتبار صفاته لا باعتبار ذاته،",
     "en": "as in “aʿjabanī Zaydun ʿilmuhu” (Zayd pleased me, his knowledge), where it is known from the outset that Zayd is pleasing with respect to his attributes, not with respect to his essence,"},
    {"type": "matn",
     "ar": "ويتضمن نسبة الإعجاب إلى «زيد» نسبته إلى صفة من صفاته إجمالا، وكذا في «سلب زيد ثوبه»،",
     "en": "and the attribution of pleasing to Zayd includes, in a general way, its attribution to one of his attributes; likewise in “suliba Zaydun thawbuhu” (Zayd was robbed, his garment)…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كما هو ظاهر كلام سيبويه.",
     "en": "As is the apparent sense of Sībawayh’s words."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ولولا المبين لم يأت به.",
     "en": "Were it not for what is explained, he would not have brought it."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فإن كون الثاني هو المقصود دون الأول ظاهر.",
     "en": "For [there] the second’s being what is intended, to the exclusion of the first, is evident."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وجعلته مناط الحكم، فكأنك قلت: جاءني زيد مع قطع النظر عن أن يكون أخاك.",
     "en": "And you made it the basis (manāṭ) of the judgement; so it is as though you said “Zayd came to me”, disregarding his being your brother."},
    {"type": "pair",
     "ar": "وإذا قلت: أكرمت زيدا أخاك، فكأنك قصدت بذلك المن على المخاطب، وأردت أن الإكرام وقع عليه من حيث إنه أخوك،",
     "en": "And when you say “akramtu Zaydan akhāka” (I honoured Zayd, your brother), it is as though you intended by it a favour to the addressee, meaning that the honouring fell on him inasmuch as he is your brother;"},
    {"type": "pair",
     "ar": "وهذه الفائدة منتفية في عطف البيان.",
     "en": "and this benefit is absent in the explicative apposition."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فلو لم تكن النسبة إلى الملابس إجمالا، بل تفصيلا لم يكن بدل الاشتمال،",
     "en": "If the attribution to what is connected were not general but specific, it would not be a substitute of inclusion."},
    {"type": "pair",
     "ar": "فلا تقول في بدل الاشتمال: قتل الأمير سيافه وبنى الوزير وكلاؤه؛ لأن للملابس مفهوما معينا.",
     "en": "So you do not say, as a substitute of inclusion, “qatala al-amīru sayyāfuhu” (the amir killed, his executioner) or “banā al-wazīru wukalāʾuhu” (the vizier built, his agents), because what is connected [here] has a determinate concept."},
]
