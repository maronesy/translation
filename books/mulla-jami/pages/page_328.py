# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 328 (printed ٣٢٧)."""

PAGE_NUMBER = 328
PRINTED_PAGE = "٣٢٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «نحو: «بسم الله» at the foot of PDF p. 327.
    {"type": "matn",
     "ar": "الرحمن الرحيم» (أو) لمجرد (الذم) نحو: «أعوذ بالله من الشيطان الرجيم»",
     "en": "…the All-Merciful, the Mercy-Giving” (bi-smi llāhi l-raḥmāni l-raḥīm); (or) for mere (censure), as in “I seek refuge in Allah from Satan the accursed” (aʿūdhu bi-llāhi mina l-shayṭāni l-rajīm);"},
    {"type": "matn",
     "ar": "(أو) لمجرد (التوكيد، مثل: ﴿نفخة واحدة﴾)؛ إذ الوحدة تفهم من التاء في «نفخة»، فأكدت بالواحدة.",
     "en": "(or) for mere (emphasis (tawkīd), as in “a single blast” (nafkhatun wāḥidatun) [translator’s reference: Qurʾān, Sūrat al-Ḥāqqa 69:13]); for oneness is understood from the tāʾ in “nafkha,” and it was then emphasized by “wāḥida” (single)."},
    {"type": "matn",
     "ar": "ولما كان غالب مواد الصفة[[١]] المشتقات، توهم كثير من النحويين أن الاشتقاق شرط في النعت حتى تأولوا غير المشتق إلى المشتق،",
     "en": "Since most of the material of the adjective (ṣifa) consists of derived words (mushtaqqāt), many grammarians supposed that derivation (ishtiqāq) is a condition of the qualifier (naʿt), so much so that they interpreted the non-derived as a derived word."},
    {"type": "matn",
     "ar": "ولما لم يكن هذا مرضيا[[٢]] للمصنف رده بقوله[[٣]]: (ولا فصل) أي: لا فرق (بين أن يكون) النعت (مشتقا أو غيره[[٤]]) في صحة وقوعه نعتا",
     "en": "Since this was not acceptable to the author, he rejected it with his words: (There is no separation), that is, no difference, (whether) the qualifier (is derived or otherwise) as regards the soundness of its occurring as a qualifier,"},
    {"type": "matn",
     "ar": "(إذا كان وضعه[[٥]]) أي: وضع غير المشتق (لغرض المعنى[[٦]]) أي: لغرض الدلالة على المعنى الواقع في المتبوع (عموما) أي: في جميع الاستعمالات",
     "en": "(when its coinage (waḍʿ)), that is, the coinage of the non-derived word, (is for the purpose of the meaning), that is, for the purpose of signifying the meaning present in the qualified word (al-matbūʿ), (generally), that is, in all usages,"},
    {"type": "matn",
     "ar": "(مثل: «تميمي» و«ذي مال») فإن «التميمي»[[٧]] يدل دائما على أن لذات",
     "en": "(as in “tamīmī” (of the tribe of Tamīm) and “dhī māl” (possessing wealth)); for “al-tamīmī” always signifies that to an essence…"},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 327 (fn ٥ there) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "تمام الماهية.",
     "en": "…the whole quiddity (tamām al-māhiyya)."},
    {"type": "pair",
     "ar": "ولم يذكرها إلحاقا لها بالمؤكدة.",
     "en": "He did not mention it, attaching it to the emphatic [adjective]."},
    {"type": "pair",
     "ar": "وههنا بحث وهو أن كلا من الطويل والعريض والعميق نعت، وليس كاشفا، والمجموع كاشف وليس نعتا.",
     "en": "There is a point for discussion here: each of “long,” “broad” and “deep” is a qualifier but not disclosing, while the aggregate is disclosing but not a qualifier."},
    {"type": "pair",
     "ar": "إن قلت: كل من تلك الأمور الثلاثة صالح لكونه كاشفا؛ لأنه مساو للجسم عند جمهور الأشاعرة؟",
     "en": "If you say: each of those three things is fit to be disclosing, since according to the majority of the Ashʿarīs it is coextensive with “body”?"},
    {"type": "pair",
     "ar": "قلنا: لا شبهة لأحد في أن المتكلم لم يقصد إلا كشف المجموع؛ لأن المجموع معرف على أن هذا الجواب لا يجري في مثل: الإنسان الحيوان الناطق،",
     "en": "We say: no one doubts that the speaker intended only the disclosure by the aggregate, because it is the aggregate that defines; moreover, this answer does not apply to such as “man, the rational animal.”"},
    {"type": "pair",
     "ar": "فالأظهر في الجواب أن يقال: إن المجموع نعت واحد إلا أن إعرابه أجرى على أجزائه كما في: قرأت الكتاب جزءا جزءا، والبيت سقف وجدران.",
     "en": "The more evident answer, then, is to say: the aggregate is a single qualifier, except that its inflection (iʿrāb) is carried on its parts, as in “I read the book part by part” and “The house is a roof and walls.”"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا حاصل كلام المصنف في شرحه.",
     "en": "This is the gist of the author’s statement in his commentary."},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: اعلم أن جمهور النحاة شرطوا في الوصف الاشتقاق، فلذلك استضعف سيبويه «مررت برجل أسد» دون «جاءني زيد أسدا» حالا.",
     "en": "Shaykh al-Raḍī said: Know that the majority of grammarians made derivation a condition of the descriptive; for that reason Sībawayh judged weak “I passed by a man [who is] a lion” but not “Zayd came to me a lion” as a circumstantial qualifier (ḥāl)."},
    {"type": "pair",
     "ar": "واعترض على الفرق وهو مندفع بأن بناء الفرق على مساعدة الاستعمال في أحدهما دون الآخر.",
     "en": "Objection was raised against the distinction, but it is repelled by the fact that the distinction rests on usage supporting the one and not the other."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "عطف الجملتين على جملتي لما، أي: ولما لم يكن إلى آخره وفي صحته نظر.",
     "en": "It is a coordination of the two clauses onto the two clauses of “lammā,” that is, “and since it was not…” to the end; and its soundness is open to question."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "بناء الرد على أنه لا داعي إلى اشتراط الاشتقاق، ولا موجب للتأويل بالمشتق لا عقلا ولا نقلا،",
     "en": "The rejection rests on there being no call to stipulate derivation and nothing that necessitates interpretation as a derived word, neither by reason nor by transmission;"},
    {"type": "pair",
     "ar": "وليس بناء الرد على الأمثلة التي ذكرها حتى يتجه ما قيل: إنه لا يخفى أن أكثر ما ذكره لا يصلح ردا؛ لأن كونه نعتا باعتبار أنه في قوة المشتق.",
     "en": "the rejection does not rest on the examples he gave, so that what has been said would apply: “It is not hidden that most of what he mentioned is unfit as a rejection, because its being a qualifier is in view of its having the force of a derived word.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الأوضح الأخصر ولا فرق بين المشتق وغيره.",
     "en": "The clearer and more concise [wording would be]: “and there is no difference between the derived and the non-derived.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "متعلق بقوله: غير مشتق.",
     "en": "It is connected with his words “non-derived.”"},
    {"type": "pair",
     "ar": "والوضع هنا يعم الوضع النوعي الشامل للوضع النوعي الذي في المجاز.",
     "en": "Coinage (waḍʿ) here includes generic coinage (al-waḍʿ al-nawʿī), which covers the generic coinage found in figurative usage (majāz)."},
    {"type": "pair",
     "ar": "فلا يرد نحو: «مررت بنسوة أربع» بناء على أن اسم العدد في المعدود مجاز،",
     "en": "So no objection arises from such as “I passed by four women,” on the basis that the number noun [used] for the counted thing is figurative;"},
    {"type": "pair",
     "ar": "ونحو: «مررت برجل أي رجل» بناء على أن «أي» هذه استفهامية استعيرت للكامل البالغ غاية الكمال في مدح أو ذم بجامع أنه مجهول الحال بحيث يحتاج إلى السؤال عنه.",
     "en": "nor from such as “I passed by a man—what a man!” on the basis that this “ayy” is interrogative, borrowed for one perfect and reaching the utmost perfection in praise or blame, the common ground being that his state is unknown, such that one needs to ask about it."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "المراد بالمعنى الحالة التي هي الدلالة. واللام للأجل.",
     "en": "By “the meaning” is meant the state which is signification. The lām denotes purpose."},
    {"type": "pair",
     "ar": "والغرض مقحمة لينص على أن اللام ليست صلة للوضع.",
     "en": "The word “purpose” (gharaḍ) is inserted to state expressly that the lām is not the complement of “coinage.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "ولذا يجب أن يكون له موصوف لفظا أو تقديرا.",
     "en": "For this reason it must have a qualified noun (mawṣūf), overt or supposed."},
]
