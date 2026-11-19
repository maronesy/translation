# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 242 (printed ٢٤١)."""

PAGE_NUMBER = 242
PRINTED_PAGE = "٢٤١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(نحو: دخلت الدار)» from the foot of PDF p. 241.
    {"type": "matn",
     "ar": "لكثرته في الاستعمال، لا لإبهامه (على الأصح) أي: على المذهب الأصح،",
     "en": "…because of its frequency in use, not because of its indefiniteness, (on the soundest [view]), that is, on the soundest doctrine;"},
    {"type": "matn",
     "ar": "فإنه ذهب بعض النحاة إلى أنه مفعول به، لكن الأصح أنه مفعول فيه، والأصل استعماله بحرف الجر، لكنه حذف لكثرة استعماله،",
     "en": "for some grammarians held that it is a direct object (mafʿūl bihi); but the soundest is that it is a mafʿūl fīhi, its base use being with a preposition, which was elided because of its frequent use."},
    {"type": "matn",
     "ar": "وهذا محل تأمل، فإن الفعل لا يطلب المفعول فيه إلا بعد تمام معناه.",
     "en": "This needs consideration; for the verb seeks the mafʿūl fīhi only after its meaning is complete."},
    {"type": "matn",
     "ar": "ولا شك أن معنى الدخول لا يتم[[١]] بدون الدار مثلا، وبعد تمام معناه بها يطلب المفعول فيه، كما إذا قلت: «دخلت الدار في البلد الفلاني»،",
     "en": "There is no doubt that the meaning of entering is not complete without “the house,” for example; and after its meaning is completed by it, it seeks the mafʿūl fīhi, as when you say: “I entered the house in such-and-such a town.”"},
    {"type": "matn",
     "ar": "فالظاهر أنه مفعول به لا مفعول فيه.",
     "en": "So it appears that it is a direct object, not a mafʿūl fīhi."},
    {"type": "matn",
     "ar": "ومما يؤيد ذلك أن كل فعل نسب إلى مكان خاص بوقوعه فيه يصح أن ينسب إلى مكان شامل له ولغيره،",
     "en": "What supports this is that every action attributed to a particular place by its occurring there may also be attributed to a place that includes it and others;"},
    {"type": "matn",
     "ar": "فإنه إذا قلت: «ضربت زيدا في الدار» التي هي جزء من البلد، فكما يصح أن تقول: «ضربت زيدا في الدار» كذلك يصح أن تقول: «ضربته في البلد»،",
     "en": "for if you say “I struck Zayd in the house,” which is part of the town, then just as it is correct to say “I struck Zayd in the house,” so it is correct to say “I struck him in the town.”"},
    {"type": "matn",
     "ar": "وفعل الدخول بالنسبة إلى الدار ليس كذلك[[٢]]، فإنه إذا قال الداخل في البلد: «دخلت الدار» لا يصح أن يقول: «دخلت البلد»،",
     "en": "The act of entering with respect to the house is not so; for when one who is inside the town says “I entered the house,” he cannot correctly say “I entered the town.”"},
    {"type": "matn",
     "ar": "فنسبة الدخول إلى الدار ليست كنسبة الأفعال إلى أمكنتها التي فعلت فيها، فلا تكون الدار مفعولا فيه، بل تكون مفعولا به.",
     "en": "So the relation of entering to the house is not like the relation of actions to the places in which they are done; hence “the house” is not a mafʿūl fīhi but a direct object."},
    {"type": "matn",
     "ar": "وقيل: معناه على الاستعمال الأصح، فيكون إشارة إلى أن استعمال «دخلت» مع «في» نحو: «دخلت في الدار» صحيح، لكن الأصح استعماله بدون «في».",
     "en": "It has been said: its meaning is “on the soundest usage,” so it indicates that using “dakhaltu” with “fī,” as in “dakhaltu fī al-dār,” is correct, but using it without “fī” is more correct."},
    {"type": "matn",
     "ar": "ونقل عن سيبويه أن استعماله بـ«في» شاذ.",
     "en": "It is reported from Sībawayh that its use with “fī” is anomalous."},
    {"type": "matn",
     "ar": "(وينتصب) أي: المفعول فيه (بعامل مضمر) بلا شريطة التفسير، نحو: «يوم الجمعة» (في جواب من قال: «متى سرت؟») أي: سرت يوم الجمعة.",
     "en": "(And it takes the accusative)—that is, the mafʿūl fīhi—(by a suppressed governor) without the condition of explanation, as in “On Friday” (in answer to one who says “When did you travel?”), that is: “I travelled on Friday.”"},
    {"type": "matn",
     "ar": "(وبعامل مضمر على شريطة التفسير) نحو: «يوم الجمعة صمت فيه»، والتفصيل فيه بعينه كما مر في المفعول به.",
     "en": "(And by a governor suppressed on the condition of explanation—ʿalā sharīṭat al-tafsīr), as in “Friday, I fasted on it”; the details here are exactly as given under the direct object."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فيكون في صلة له كما أن عن صلة لضده الذي هو الخروج",
     "en": "So “fī” is its connective particle (ṣila), just as “ʿan” is the connective of its opposite, which is going out (khurūj)."},
    {"type": "pair",
     "ar": "استدل الشيخ الرضي على أن الدخول لازم بلزوم كلمة «في» في غير المكان ودخولها في المكان.",
     "en": "Shaykh al-Raḍī argued that “dukhūl” is intransitive from the obligatory use of the word “fī” with what is not a place, and its entering [also] with place."},
    # REVIEW: print reads «ويكون الدخول فعلا» (sense requires «فعولا», the pattern fuʿūl); transcribed as printed.
    {"type": "pair",
     "ar": "ويكون الدخول فعلا، والفعول من المصادر اللازمة غالبا، وبكونه ضد الخروج وهو لازم.",
     "en": "[He argued also] from “dukhūl” being on the pattern fuʿūl, and fuʿūl is mostly among the maṣdars of intransitive verbs; and from its being the opposite of “khurūj,” which is intransitive."},
    {"type": "pair",
     "ar": "ولا يخفى أن ما ذكره يدل على نفي التعدي بلا واسطة.",
     "en": "It is not hidden that what he mentioned indicates the denial of transitivity without an intermediary."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه أنه يصح ذلك في دخلت الباب، دخلت الدهليز، دخلت الدار.",
     "en": "Against this: that holds in “I entered the door, I entered the vestibule, I entered the house.”"},
    {"type": "pair",
     "ar": "وإذا كان الباب مفعولا فيه فكذلك كل ما بعد \"دخلت\".",
     "en": "And if “the door” is a mafʿūl fīhi, so is everything after “dakhaltu.”"},
]
