# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 139 (printed ١٣٨)."""

PAGE_NUMBER = 139
PRINTED_PAGE = "١٣٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "يسم فاعله (ضارع) أي: عاجز ذليل، وهو فاعل الفعل المحذوف، أي: «يبكيه ضارع[[١]]» بقرينة السؤال المقدر[[٢]]، وهو «من يبكيه؟».",
     "en": "…whose agent is not named: (ḍāriʿ) — that is, one who is powerless and abased; and it is the agent of the elided verb — i.e., “A powerless one weeps for him,” by the indication of the implied question, which is “Who weeps for him?”"},
    {"type": "matn",
     "ar": "وأما على رواية «ليبك يزيد» على البناء للفاعل، ونصب «يزيد» فليس مما نحن فيه[[٣]].",
     "en": "As for the variant reading “Let [him] weep for Yazīd” — in the active voice, with “Yazīd” in the accusative — it does not belong to what we are discussing."},
    {"type": "matn",
     "ar": "(لخصومة[[٤]]) متعلق بـ«ضارع»[[٥]] أي: يبكيه من يذل ويعجز عن مقاومة الخصماء؛ لأنه كان ظهيرا للعجزة والأذلاء، وآخر البيت:",
     "en": "“For a dispute” (li-khuṣūma) is attached to “ḍāriʿ” — that is, he is wept for by one who is humbled and unable to withstand adversaries, because he [Yazīd] was a support for the incapable and the lowly. And the end of the verse [is]:"},
    {"type": "verse",
     "ar": "................    ومختبط مما تطيح[[٦]] الطوائح",
     "en": "… and a distraught seeker, [brought low] by that which the felling misfortunes cast down."},
    {"type": "matn",
     "ar": "والمختبط: السائل من غير وسيلة[[٧]].",
     "en": "“Al-mukhtabiṭ” is one who asks for aid without any prior means of connection."},
    {"type": "matn",
     "ar": "والإطاحة: الإهلاك.",
     "en": "And “al-iṭāḥa” means destruction."},
    {"type": "matn",
     "ar": "و«الطوائح»: جمع «مطيحة»[[٨]] على غير القياس كـ«لواقح» جمع «ملقحة»[[٩]].",
     "en": "And “al-ṭawāʾiḥ” is the plural of “muṭīḥa” — irregularly (against analogy) — like “lawāqiḥ,” the plural of “mulqiḥa.”"},

    {"type": "rule"},

    # -------- continuation of footnote ٧ from the previous page (printed ١٣٧) --------
    {"type": "note", "num": "…"},
    {"type": "pair",
     "ar": "المناسب للمقام أن يدعى أن «الضارع» و«المختبط» لما وقعا في شدة ونقمة بسبب موتك يا يزيد ناسب أن يبكى عليهما دونك؛ لأنك في رخاء ونعمة.",
     "en": "…what befits the context is to claim that “the abased” (al-ḍāriʿ) and “the distraught” (al-mukhtabiṭ), since they have fallen into hardship and calamity on account of your death, O Yazīd, it is fitting that they be wept over rather than you — because you are in ease and blessing."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "نكرة مفيدة للعموم وإن كان في حيز الإثبات مثل «تمرة خير من جرادة»، كما هو المناسب لمقام المدح، وإليه أشار بقوله: أي: يبكيه من يذل، إلا أن العموم عرفي لا حقيقي كما لا يخفى.",
     "en": "[Ḍāriʿ] is an indefinite noun conveying generality, even though it occurs in an affirmative context — like “A [single] date is better than a locust” — as befits the setting of praise; to this he pointed by his words: “that is, he is wept for by one who is humbled.” Save that the generality is conventional, not literal, as is not hidden."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "المدلول عليه بلفظ المبني للمفعول، فإنه منشأ للالتباس والتردد، وهو منشأ للسؤال، فنزل السبب منزلة المسبب.",
     "en": "[The implied question is] that indicated by the passive-voice wording, for it is the source of ambiguity and hesitation, which is in turn the source of the question; so the cause has been placed in the position of the effect."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وعلى البناء للمفعول أيضا لو جعل «يزيد» منادى حذف حرف ندائه، وجعل مضارع مفعول ما لم يسم فاعله «ليبك» لا يكون مما نحن فيه. نقل هذا التوجيه عن المولى الرومي.",
     "en": "On the passive reading as well: if “Yazīd” were taken as a vocative whose vocative particle has been elided, and “liyubka” were taken as an imperfect passive verb with unnamed agent, it would not belong to what we are discussing. This construal is transmitted from al-Mawlā al-Rūmī."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "اللام للأجل كما هو الظاهر. وحينئذ يراد بالخصومة خصومة غيره. ويحتمل أن يكون للوقت، وحينئذ يحتمل خصومته وخصومة غيره.",
     "en": "The lām [in “li-khuṣūma”] denotes purpose, as is apparent; on that reading, by “dispute” is meant the dispute of another. It may also denote time, in which case it admits both his own dispute and another’s."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وإن لم يعتمد على شيء؛ لأن الجار يكتفي برائحة من الفعل، لا بـ«يبكيه» المقدر؛ لأن هذا البكاء بكاء فوته، لا بكاء الخصومة مع أنها ليست سببا قريبا للبكاء.",
     "en": "[It is attached to “ḍāriʿ”] even though [ḍāriʿ] does not rest upon anything governing it, because the preposition is satisfied with a mere whiff of a verb — not by the implied “weeps for him,” since this weeping is the weeping over his loss, not the weeping of the dispute, especially as [the dispute] is not a proximate cause of the weeping."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "حكاية حال ماضية قد يورد الماضي بصورة الحال إذا كان الأمر هائلا لاستقراره في الخيال مع بقاء أثره.",
     "en": "[It is] the narration of a past state: the past may be rendered in the form of the present when the matter is momentous, on account of its being fixed in the imagination together with the persistence of its effect."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "أي: بغير علقة وسابقة حق، يقال: اختبطني فلان، وأصله من خبطت الشجرة إذا ضربتها بالعصا ليسقط ورقها.",
     "en": "That is, without any bond or prior claim of right. One says “so-and-so came to me seeking bounty (ikhtabaṭanī)”; its origin is from “I beat the tree” (khabaṭtu l-shajara), i.e., when you strike it with a stick so that its leaves fall."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "بمعنى مهلكة على خلاف القياس، يعني: على حذف الزوائد من المزيد كما يقال: «أعشب فهي عاشب». وملقحة من الإلقاح.",
     "en": "[Muṭīḥa is] in the sense of “destroying,” against analogy — meaning by dropping the augmentative letters from the augmented [participle], as one says “aʿshaba, so it is ʿāshib.” And “mulqiḥa” is from “ilqāḥ” (impregnation)."},
    {"type": "pair",
     "ar": "قال عبد الغفور: قوله: «والطوائح جمع مطيحة» على حذف الزوائد، كما يقال: «أعشب فهو عاشب»، ولا يقال: «مطيحات» على القياس. ويجوز أن يكون جمع «طائحة» للنسبة، مثل: «ماء دافق»، يقال: طاح يطوح وطاح يطيح، أي: ذهب.",
     "en": "ʿAbd al-Ghafūr said: His words “al-ṭawāʾiḥ is the plural of muṭīḥa” [mean it is so] by dropping the augmentative letters, as one says “aʿshaba, so it is ʿāshib”; and one does not say “muṭīḥāt” by analogy. It may also be the plural of “ṭāʾiḥa” [formed] for the relational sense, like “water pouring forth (māʾ dāfiq)”; one says ṭāḥa yaṭūḥu and ṭāḥa yaṭīḥu, i.e., it perished / went away."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "الأولى أن يقال: جمع «ملقح»؛ لأن المراد منه الفحل. واللواقح: الرياح التي تهب في الربيع. وتحمل الأشجار بسببها وتتزهر.",
     "en": "It would be better to say “the plural of mulqiḥ,” because what is meant by it is the male [pollinator]. Al-lawāqiḥ are the winds that blow in spring, by whose agency the trees bear [fruit] and blossom."},
]
