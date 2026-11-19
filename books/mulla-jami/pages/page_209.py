# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 209 (printed ٢٠٨)."""

PAGE_NUMBER = 209
PRINTED_PAGE = "٢٠٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "وقعت توابع أولى؛ لأن حرف النداء لا يباشرها",
     "en": "…they occur as appositives is all the more fitting, because the vocative particle is not directly attached to them;"},
    {"type": "matn",
     "ar": "مثل: «يا تميم كلهم»[[١]] في التأكيد، و«يا زيد ذا المال» في الصفة، و«يا رجل أبا عبد الله» في عطف البيان،",
     "en": "such as “O Tamīm, all of them” (yā Tamīmu kullahum) for the corroborative, “O Zayd, possessor of wealth” (yā Zaydu dhā al-māli) for the qualifier, and “O man, Abū ʿAbd Allāh” (yā rajulu abā ʿAbdi llāhi) for the explicative apposition;"},
    {"type": "matn",
     "ar": "ولا يجيء المعطوف بحرف الممتنع دخول «يا» عليه مضافا؛ لأن اللام يمتنع دخولها على المضاف بالإضافة الحقيقية.",
     "en": "the noun coordinated by a particle on which the entry of “yā” is barred does not occur annexed, because the lām cannot enter a noun annexed by genuine annexation."},
    {"type": "matn",
     "ar": "(والبدل والمعطوف غير ما ذكر[[٢]]) أي: غير المعطوف الذي ذكر من قبل، وهو المعطوف الممتنع دخول «يا» عليه، فغيره المعطوف الذي لا يمتنع دخول «يا» عليه.",
     "en": "(And the substitute, and the coordinated noun other than what has been mentioned), that is, other than the coordinated noun mentioned before, namely the one on which the entry of “yā” is barred; so the other is the coordinated noun on which the entry of “yā” is not barred."},
    {"type": "matn",
     "ar": "(حكمه[[٣]]) أي: حكم كل واحد منهما (حكم المنادى المستقل) الذي باشره حرف النداء،",
     "en": "(Its rule), that is, the rule of each of the two, (is the rule of the independent vocative) to which the vocative particle is directly attached;"},
    {"type": "matn",
     "ar": "وذلك لأن البدل هو المقصود بالذكر، والأول كالتوطئة لذكره،",
     "en": "that is because the substitute is what is intended by the mention, the first being like a preparation for mentioning it;"},
    {"type": "matn",
     "ar": "والمعطوف المخصوص[[٤]] هو المنادى المستقل في الحقيقة، ولا مانع من دخول حرف النداء عليه، فيكون حرف النداء مقدرا فيه",
     "en": "and the particular coordinated noun is in reality the independent vocative, and nothing prevents the vocative particle from entering it; so the vocative particle is implied in it."},
    {"type": "matn",
     "ar": "(مطلقا) أي: حال كون كل واحد منهما[[٥]] مطلقا[[٦]] في هذا الحكم[[٧]] غير مقيد بحال من الأحوال،",
     "en": "(Unrestrictedly), that is, each of them being unrestricted in this rule, not bound by any one state,"},
    {"type": "matn",
     "ar": "أي: سواء كانا مفردين، أو مضافين، أو مضارعين للمضاف أو نكرتين،",
     "en": "that is, whether they are singular, annexed, resembling the annexed, or indefinite."},
    {"type": "matn",
     "ar": "فالبدل مثل: «يا زيد بشر، ويا زيد أخا عمرو، ويا زيد طالعا جبلا، ويا زيد رجلا صالحا»،",
     "en": "The substitute is like: “O Zayd, Bishr”; “O Zayd, brother of ʿAmr”; “O Zayd, one climbing a mountain”; and “O Zayd, a righteous man.”"},
    {"type": "matn",
     "ar": "والمعطوف مثل: «يا زيد وعمرو»، و«يا زيد وأخا عمرو»، و«يا زيد وطالعا جبلا»، و«يا زيد ورجلا صالحا».",
     "en": "The coordinated noun is like: “O Zayd and ʿAmr”; “O Zayd and brother of ʿAmr”; “O Zayd and one climbing a mountain”; and “O Zayd and a righteous man.”"},
    {"type": "matn",
     "ar": "(والعلم) أي: العلم المنادى المبني على الضم[[٨]]:",
     "en": "(And the proper name), that is, the vocative proper name built on the ḍamma:"},
    {"type": "matn",
     "ar": "إما كونه منادى؛ فلأن الكلام فيه، وإما كونه مبنيا على الضم فلما يفهم من اختيار فتحة المبني عن جواز ضمه[[٩]]،",
     "en": "as for its being a vocative, that is because the discussion concerns it; and as for its being built on the ḍamma, that is from what is understood by preferring the fatḥa of the indeclinable over the permissibility of its ḍamma,"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "نظرا إلى أن «تميما» في نفسه غائب. وجوز الشيخ الرضي «كلكم» نظرا إلى الخطاب العارض.",
     "en": "In view of “Tamīm” being in itself a third person. Shaykh al-Raḍī allowed “kullakum” (all of you), in view of the accidental address."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "صفة أو بدل.",
     "en": "[Ghayru is] a qualifier or a substitute."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: حكم كل واحد منهما، ويجوز إرجاع الضمير إلى مجموعهما بتأويلهما بما بقي،",
     "en": "That is: the rule of each of the two; the pronoun may also be referred to the two together, by interpreting them as “what remains,”"},
    {"type": "pair",
     "ar": "فعلى هذا لو قال: وما بقي حكمه حكم المستقل لكان أخصر.",
     "en": "and on this, had he said “and what remains has the rule of the independent [vocative],” it would have been shorter."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: الممتاز من بين التوابع بعدم امتناع دخول «يا» عليه، وهو المجرد عن حرف التعريف.",
     "en": "That is: the one distinguished among the appositives by the entry of “yā” not being barred on it, namely the one stripped of the article of definiteness."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أو الضمير إليهما بتأويلهما بما بقي من التوابع، فيعلم منه أنه لو قال: وما بقي حكمه حكم المستقل لكان أخصر.",
     "en": "Or the pronoun [refers] to the two, interpreting them as “the remaining appositives”; from which it is known that had he said “and what remains has the rule of the independent [vocative],” it would have been shorter."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "وحال كون كل منهما تابعا لمفرد أو مضاف.",
     "en": "And whether each of them is an appositive to a singular or to an annexed noun."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: في كونه كالمنادى المستقل الذي باشره حرف النداء، وفيه لطافة.",
     "en": "That is: in its being like the independent vocative to which the vocative particle is directly attached; and there is a subtlety in this."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "فخرج «عبد الله» و«زيدان» و«زيدون» إذا جعلتهما علما.",
     "en": "Thus “ʿAbd Allāh” is excluded, as are “Zaydān” and “Zaydūn” when you make them proper names."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "لأنه لم يعرف من البناء إلا البناء على الضم أو الفتح،",
     "en": "Because no indeclinability is known [here] except being built on the ḍamma or the fatḥa;"},
    {"type": "pair",
     "ar": "وفيه نظر لجواز أن ينبئ اختيار الفتح عن جواز الجر في «يا لزيد بن معيث».",
     "en": "but this is open to objection, since the preference for the fatḥa might indicate the permissibility of the genitive, as in “yā la-Zaydi bni Muʿayth.”"},
]
