# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 161 (printed ١٦٠)."""

PAGE_NUMBER = 161
PRINTED_PAGE = "١٦٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(والخبر: قد يكون جملة[[١]]):",
     "en": "…(And the khabar may be a sentence—wa-l-khabaru qad yakūnu jumlatan):"},
    {"type": "matn",
     "ar": "١-اسمية (مثل: «زيد أبوه قائم»).",
     "en": "1. nominal (ismiyya), (as in: “Zayd, his father is standing”—Zaydun abūhu qāʾimun)."},
    {"type": "matn",
     "ar": "٢-(و) فعلية، مثل: («زيد قام أبوه») ولم يذكر الظرفية[[٢]]؛ لأنها راجعة إلى الفعلية[[٣]].",
     "en": "2. (And) verbal (fiʿliyya), as in: (“Zayd, his father stood”—Zaydun qāma abūhu). He did not mention the adverbial [sentence] (ẓarfiyya), because it reduces to the verbal."},
    {"type": "matn",
     "ar": "وإذا كان الخبر جملة، والجملة مستقلة بنفسها لا يقتضي الارتباط بغيرها",
     "en": "When the khabar is a sentence—and a sentence is self-standing and does not require connection with anything else—"},
    {"type": "matn",
     "ar": "(فلا بد) في الجملة الواقعة خبرا عن المبتدأ (من عائد[[٤]]) يربطها به،",
     "en": "(then there must be) in the sentence occurring as khabar of the mubtadaʾ (a referent—ʿāʾid) that links it to it."},
    {"type": "matn",
     "ar": "وذلك العائد إما ضمير كما في المثالين المذكورين أو غيره:",
     "en": "That referent is either a pronoun, as in the two examples mentioned, or something else:"},
    {"type": "matn",
     "ar": "كاللام في «نعم الرجل[[٥]] زيد»، ووضع المظهر موضع المضمر[[٦]] في نحو: ﴿الحاقة ما الحاقة﴾[[٧]]،",
     "en": "such as the lām [of the article] in “Excellent is the man, Zayd” (niʿma al-rajulu Zaydun), and the placing of the overt noun in the position of the pronoun, as in: “The Inevitable—what is the Inevitable?”"},
    {"type": "matn",
     "ar": "وكون الخبر تفسيرا للمبتدأ[[٨]] نحو: ﴿قل هو الله أحد﴾[[٩]].",
     "en": "and the khabar’s being an explication (tafsīr) of the mubtadaʾ, as in: “Say: He is Allah, One.”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لم يقيد بكونها خبرية، فكأنه تبع جمهور النحاة في أن الإنشائية، ولو كانت قسمية صح أن تكون خبرا للمبتدأ،",
     "en": "He did not restrict it to its being declarative (khabariyya); so it is as if he followed the majority of the grammarians in [holding] that the performative [sentence] (inshāʾiyya), even if it is an oath (qasamiyya), may validly be the khabar of the mubtadaʾ."},
    {"type": "pair",
     "ar": "ومنهم من منعوا متمسكين بما لا طائل تحته،",
     "en": "Among them are those who forbade it, holding on to what has no substance to it."},
    {"type": "pair",
     "ar": "وقد تبع السيد الشريف هؤلاء متمسكا بأن الخبر يجب أن يكون حالا من أحوال المبتدأ، والإنشاء ليس حالا من أحواله إلا بتأويل،",
     "en": "Al-Sayyid al-Sharīf followed these, holding that the khabar must be one of the states of the mubtadaʾ, whereas the performative is not one of its states except by interpretation (taʾwīl);"},
    {"type": "pair",
     "ar": "مثلا إذا قلت: «زيد اضربه»، فطلب الضرب صفة قائمة بالمتكلم ليست من أحوال «زيد»",
     "en": "for example, when you say “Zayd—strike him” (Zaydun iḍribhu), the demand for striking is an attribute subsisting in the speaker, not one of the states of “Zayd,”"},
    {"type": "pair",
     "ar": "إلا باعتبار كونه متعلقا للطلب، أو كونه مقولا في حقه، واستحقاقه أن يقال فيه ذلك.",
     "en": "except in respect of his being the object of the demand, or its being said concerning him, and his deserving that this be said of him."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لم يذكر الشرطية أيضا، لأن الشرط عند أهل العربية قيد للجزاء، كما هو المشهور،",
     "en": "He did not mention the conditional [sentence] (sharṭiyya) either, because the condition, according to the scholars of Arabic, is a qualification of the apodosis (jazāʾ), as is well known;"},
    {"type": "pair",
     "ar": "والجزاء اسمية أو فعلية ولو بالآخرة.",
     "en": "and the apodosis is nominal or verbal, even if [only] ultimately."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "بمعنى أنها نائبة عن الفعلية، وإلا فالظرفية جملة لانتقال إسناد الفعل إلى الظرف، ولهذا استتر فيه ضمير كان فاعلا للفعل.",
     "en": "In the sense that it stands in for the verbal [sentence]; otherwise the adverbial is a sentence [in its own right], because the predication of the verb has passed to the adverbial—and for this reason a pronoun that was the agent of the verb is concealed in it."},
    {"type": "pair",
     "ar": "ولك أن تقول: لم يذكرها لأنها سبقت غير مرة، بل متصلا بهذه المسألة.",
     "en": "You may say: he did not mention it because it has come up more than once—indeed, directly adjoining this question."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "جواب شرط محذوف، أي: إذا كان جملة فلا بد من عائد.",
     "en": "[This is] the apodosis of an elided condition, that is: “if it is a sentence, there must be a referent.”"},
    {"type": "pair",
     "ar": "وكذا في الخبر المفرد المشتق أو المؤول به أيضا.",
     "en": "Likewise in the single khabar that is derived (mushtaqq) or interpreted as such."},
    {"type": "pair",
     "ar": "ووجه التخصيص بالجملة أن العائد في الخبر المفرد غير لازم كما إذا لم يكن مشتقا نحو: «زيد إنسان أو جسم».",
     "en": "The reason for restricting [the statement] to the sentence is that the referent is not necessary in the single khabar, as when it is not derived, as in: “Zayd is a human” or “a body.”"},
    {"type": "pair",
     "ar": "وقال الكسائي: لا بد في خبر كان مطلقا من عائد حتى قال: معنى كان زيد أخوك هو.",
     "en": "Al-Kisāʾī said: a referent is required in a khabar of whatever kind, so much so that he said: the meaning of “Zayd is your brother” is “Zayd is your brother, he.”"},
    # REVIEW: printed clearly «معنى كان زيد أخوك هو»; the «كان» is syntactically odd here (possibly a misprint); transcribed as printed, translated by the evident sense.

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا يخفى أن «نعم الرجل» من قبيل وضع الظاهر موضع المضمر إلا أن الظاهر صلح لوضعه موضع المضمر باعتبار لام العهد،",
     "en": "It is not hidden that “niʿma al-rajulu” belongs to the category of placing the overt noun in the position of the pronoun, except that the overt noun became fit to be placed in the position of the pronoun by virtue of the lām of prior reference (lām al-ʿahd);"},
    {"type": "pair",
     "ar": "فلا معنى لجعله قسيما له.",
     "en": "so there is no sense in making it a separate co-division of it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "جاز مقام التعظيم مطلقا، وفي غيره جاز في جملتين مطلقا، هذا في سعة الكلام.",
     "en": "It is permitted in the context of magnification (taʿẓīm) without restriction, and outside it, it is permitted across two sentences without restriction; this is in the latitude of [ordinary] speech."},
    {"type": "pair",
     "ar": "وفي الشعر جاز عند سيبويه بشرط أن يكون بلفظ الأول، وعند الأخفش مطلقا.",
     "en": "In poetry it is permitted according to Sībawayh on condition that it be in the wording of the first [occurrence], and according to al-Akhfash without restriction."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "سورة الحاقة:٢.",
     "en": "Qurʾān, Sūrat al-Ḥāqqa 69:2."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "الأولى عين المبتدأ ليشمل قولنا: الشأن زيد قائم، ومقول عمرو قائم.",
     "en": "It would be better [to say] “identical with the mubtadaʾ,” so as to include our saying: “The matter is: Zayd is standing” (al-shaʾnu Zaydun qāʾimun), and “What ʿAmr says is: [Zayd] is standing.”"},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "الإخلاص:١.",
     "en": "Qurʾān, Sūrat al-Ikhlāṣ 112:1."},
]
