# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 418 (printed ٤١٧)."""

PAGE_NUMBER = 418
PRINTED_PAGE = "٤١٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «وبناء «عوض»» from PDF p. 417.
    {"type": "matn",
     "ar": "على الضم لكونه مقطوعا من الإضافة[[١]] كـ«قبل وبعد» بدليل إعرابه[[٢]] مع المضاف إليه[[٣]] نحو: «عوض العائضين» أي: دهر الداهرين،",
     "en": "…on ḍamma, because it is cut off from annexation, like “qablu” and “baʿdu”, as shown by its being declined together with the second term of annexation, as in “ʿawḍa l-ʿāʾiḍīna”, that is, “dahra l-dāhirīna” (for ever and ever);"},
    {"type": "matn",
     "ar": "ومعنى «الداهر والعائض»: الذي يبقى على وجه الدهر.",
     "en": "the meaning of “al-dāhir” and “al-ʿāʾiḍ” is that which endures through time."},
    {"type": "matn",
     "ar": "(والظروف المضافة إلى الجملة و) إلى كلمة (إذ) المضافة إلى الجملة (يجوز بناؤها) لاكتسابها البناء من المضاف إليه ولو بواسطة (على الفتح) للخفة،",
     "en": "(And the adverbials annexed to a sentence, and) to the word (“idh”), which is annexed to a sentence: (their indeclinability is permissible), since they acquire indeclinability from the second term of annexation, even if through an intermediary, (on fatḥa), for lightness,"},
    {"type": "matn",
     "ar": "نحو قوله تعالى: ﴿يوم ينفع الصادقين﴾[[٤]]، وقوله تعالى: ﴿ومن خزي يومئذ﴾[[٥]] فيمن قرأ بالفتح،",
     "en": "as in His words, the Exalted: “yawma yanfaʿu l-ṣādiqīna” (the day on which [their truthfulness] will benefit the truthful), and His words, the Exalted: “wa-min khizyi yawmaʾidhin” (and from the disgrace of that day), according to those who read it with fatḥa."},
    {"type": "matn",
     "ar": "ويجوز إعرابها أيضا لكونها أسماء مستحقة للإعراب، ولا يجب اكتساب المضاف إلى المبني البناء منه.",
     "en": "Their declension is also permissible, since they are nouns that merit declension, and it is not necessary that what is annexed to an indeclinable word acquire indeclinability from it."},
    {"type": "matn",
     "ar": "(كذلك) أي: كالمذكور من الظروف في جواز البناء على الفتح والإعراب («مثل» و«غير») مذكورين (مع «ما» و«أن») مخففة أو مشددة،",
     "en": "(Likewise), that is, like the adverbials mentioned, in that both indeclinability on fatḥa and declension are permissible, are (“mithl” and “ghayr”) when they are mentioned (with “mā” and “an”), lightened or doubled,"},
    {"type": "matn",
     "ar": "مثل: «قيامي مثل ما قام زيد» و«قيامي مثل أن يقوم أو مثل أنك تقوم»؛",
     "en": "as in “qiyāmī mithla mā qāma zaydun” (my standing is like Zayd’s standing) and “qiyāmī mithla an yaqūma” or “mithla annaka taqūmu” (my standing is like his standing / like your standing),"},
    {"type": "matn",
     "ar": "لمشابهتهما الظروف المضافة إلى الجملة نحو: «إذا وحيث»، وبهذه المشابهة ذكرهما في بحث الظروف،",
     "en": "because they resemble the adverbials annexed to a sentence, such as “idhā” and “ḥaythu”; it is because of this resemblance that he mentioned them in the discussion of adverbials."},
    {"type": "matn",
     "ar": "ويجوز إعرابهما لكونهما اسمين مستحقين للإعراب.",
     "en": "Their declension is permissible, since they are two nouns that merit declension."},

    {"type": "section", "ar": "[المعرفة والنكرة]",
     "en": "The Definite and the Indefinite Noun"},

    {"type": "matn",
     "ar": "(المعرفة والنكرة[[٦]]) أي: هذا باب بيان المعرفة والنكرة من أقسام الاسم[[٧]].",
     "en": "(The definite and the indefinite), that is, this is the chapter explaining the definite and the indefinite, among the divisions of the noun."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا يقتضي استدراك ذكره بعد ذكر الغايات.",
     "en": "This entails that mentioning it after the mention of the ghāyāt (adverbials cut off from annexation) is redundant."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فإن الإضافة إلى المفرد ترجح جانب الإعراب لاختصاص فائدته من التعريف التخصيص والتخفيف بالمعرب.",
     "en": "For annexation to a single word favours the side of declension, because its benefit—definiteness, specification and lightening—is peculiar to the declinable."},
    {"type": "pair",
     "ar": "وإذا تعرب الغايات عند الإضافة إلى المفرد، فالقول بأنه يجوز أن يكون عوض المضاف مبنيا مفتوحا؛ لأنه جاء فيه الفتح لا معربا منصوبا كما وهم ليس بشيء.",
     "en": "Since the ghāyāt are declined when annexed to a single word, the claim that annexed “ʿawḍ” may be indeclinable with fatḥa—because fatḥa has come in it—and not declinable in the accusative, as someone imagined, is of no account."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الدليل غير محكم لجواز أن يكون ما يرى منصوبا ومفتوحا بالبناء؛",
     "en": "The proof is not conclusive, since what appears accusative may be [a form] with fatḥa by indeclinability;"},
    {"type": "pair",
     "ar": "لأن «عوض» جاء مفتوحا ومجيئه مكسورا ومفتوحا يبعده عن كونه مقطوعا عن الإضافة؛ لأن نظائره لا يكون إلا مضموما.",
     "en": "for “ʿawḍ” has come with fatḥa, and its coming with kasra and with fatḥa makes it unlikely that it is cut off from annexation, since its counterparts occur only with ḍamma."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة المائدة: ١١٩.",
     "en": "Qurʾān, Sūrat al-Māʾida 5:119."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة هود: ٦٦.",
     "en": "Qurʾān, Sūrat Hūd 11:66."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "هذا باب بيان المعرفة والنكرة أتى بهما معرفتين؛ لأنهما لكثرة ذكرهما فيما سبق معهودتان،",
     "en": "“This is the chapter explaining the definite and the indefinite”: he gave them in definite form because, having been mentioned often before, they are already known;"},
    {"type": "pair",
     "ar": "وكان كثرة احتياج المباحث المقدمة إليهما داعية إلى تقديمهما على بيان المنصرف وغير المنصرف إلا أنه أخرهما لتوقف معرفة بعض أقسام المعرفة على مباحث المبني إلى هذا المقام.",
     "en": "and the frequent need of the earlier discussions for them called for placing them before the treatment of the declinable and the diptote, but he put them later because knowing some divisions of the definite depends on the discussions of the indeclinable up to this point."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "نبه بذلك على أنهما من مباحث الاسم كالمعرب والمبني لبعد العهد",
     "en": "By this he drew attention to their being among the topics of the noun, like the declinable and the indeclinable, because the earlier mention is far off,"},
    {"type": "pair",
     "ar": "بوضع جزئي بأن يلاحظ الموضوع والموضوع له بخصوصهما لا بخصوصية الطرفين، أو كلي بأن يلاحظ الموضوع بوجه أعم",
     "en": "[and the coinage is either] by particular coinage, in which the coined expression and what it is coined for are considered in their particularity, not by the particularity of the two terms, or by universal coinage, in which the coined expression is considered in a more general respect…"},
]
