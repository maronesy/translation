# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 147 (printed ١٤٦)."""

PAGE_NUMBER = 147
PRINTED_PAGE = "١٤٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "جاز حذفه؛ لئلا يتوهم[[١]] أن مفعول الفعل الثاني مغاير للمذكور،",
     "en": "…its elision is permissible; lest it be imagined that the object of the second verb is other than the one mentioned;"},
    {"type": "matn",
     "ar": "ويكون الضمير حينئذ راجعا إلى لفظ متقدم رتبة، كما تقول: «ضربني وأكرمته زيد»",
     "en": "and the pronoun in that case refers back to an expression that precedes in rank, as you say: “Zayd struck me and I honored him” (ḍarabanī wa-akramtuhu Zaydun)"},
    {"type": "matn",
     "ar": "(إلا أن يمنع مانع[[٢]]) من الإضمار، كما هو القول المختار، ومن الحذف كما هو القول الغير المختار،",
     "en": "(unless some impediment prevents—illā an yamnaʿa māniʿun) concealment, as is the preferred view, or elision, as is the non-preferred view;"},
    {"type": "matn",
     "ar": "(فتظهر) المفعول، فإنه إذا امتنع الإضمار والحذف لا سبيل إلا إلى الإظهار،",
     "en": "(then you make) the object (overt—fa-tuẓhira); for when concealment and elision are precluded, there is no way except to making [it] overt,"},
    {"type": "matn",
     "ar": "نحو: «حسبني وحسبتهما منطلقين الزيدان منطلقا» حيث أعمل «حسبني»، فجعل[[٣]] «الزيدان» فاعلا له، و«منطلقا» مفعولا له،",
     "en": "as in: “The two Zayds deemed me setting off, and I deemed them setting off” (ḥasibanī wa-ḥasibtuhumā munṭaliqayn al-Zaydān munṭaliqan), where he made “ḥasibanī” govern, making “al-Zaydān” its agent and “munṭaliqan” its object,"},
    {"type": "matn",
     "ar": "وأضمر المفعول الأول في «حسبتهما»، وأظهر المفعول الثاني وهو «منطلقين» لمانع،",
     "en": "and concealed the first object in “ḥasibtuhumā,” and made the second object, namely “munṭaliqayn,” overt because of an impediment;"},
    {"type": "matn",
     "ar": "وهو أنه لو أضمر مفردا خالف المفعول الأول[[٤]]، ولو أضمر مثنى خالف المرجع، وهو قوله: «منطلقا».",
     "en": "namely that, had he concealed a singular, it would disagree with the first object; and had he concealed a dual, it would disagree with the referent, which is his word “munṭaliqan.”"},
    {"type": "matn",
     "ar": "ولا يخفى أنه لا يتصور التنازع[[٥]] في هذه الصورة، إلا إذا لاحظت المفعول الثاني اسما دالا على اتصاف ذات ما بالانطلاق من غير ملاحظة تثنيته وإفراده،",
     "en": "It is not hidden that tanāzuʿ is inconceivable in this case unless you regard the second object as a noun indicating that some entity is qualified by setting off, without regard to its being dual or singular;"},
    {"type": "matn",
     "ar": "وإلا فالظاهر أنه لا تنازع بين الفعلين[[٦]] في المفعول الثاني؛ لأن الأول يقتضي مفعولا مفردا، والثاني مفعولا مثنى، فلا يتوجهان إلى أمر واحد، فلا تنازع.",
     "en": "otherwise, what is apparent is that there is no tanāzuʿ between the two verbs over the second object; because the first requires a singular object and the second a dual object, so they are not directed to a single thing, and so there is no contention."},
    {"type": "matn",
     "ar": "ولما استدل[[٧]] الكوفيون على أولوية إعمال الفعل الأول بقول امرئ القيس:",
     "en": "When the Kūfans argued for the priority of making the first verb govern from the verse of Imruʾ al-Qays:"},
    {"type": "verse",
     "ar": "ولو أن ما أسعى لأدنى معيشة          كفاني ولم أطلب قليل من المال",
     "en": "Were it that I strove for the meanest livelihood, a little wealth would have sufficed me, and I would not have sought [more]."},
    {"type": "matn",
     "ar": "حيث قالوا: قد توجه الفعلان، أعني: «كفاني ولم أطلب» إلى اسم واحد وهو «قليل من المال»، فاقتضى الأول رفعه بالفاعلية، والثاني نصبه بالمفعولية، وامرؤ",
     "en": "in that they said: the two verbs—I mean “kafānī” and “lam aṭlub”—are directed to a single noun, namely “qalīlun min al-māl”; the first requires it in the nominative as agent, and the second in the accusative as object; and Imruʾ…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإن قلت: كون المختار عدم الحذف لا يحتاج إلى بيان سبب؛ لأنه الأصل؟",
     "en": "If you say: that non-elision is the preferred [course] needs no explanation of a cause, since it is the default (al-aṣl)?"},
    {"type": "pair",
     "ar": "قلت: ليس الأصل مختارا مطلقا، بل إذا لم يدع داع إلى خلافه، وإلا لكان الذكر مختارا مطلقا، والحقيقة مختارة مطلقا دون المجاز،",
     "en": "I say: the default is not preferred absolutely, but only when nothing calls for its contrary; otherwise mention would be preferred absolutely, and the literal (ḥaqīqa) preferred absolutely over the figurative (majāz);"},
    {"type": "pair",
     "ar": "فلا بد لكونه مختارا مطلقا من أمر زائد على الأصالة، وهو هنا ما ذكره.",
     "en": "so for its being preferred absolutely there must be something beyond its being the default, and that, here, is what he mentioned."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: أضمرت في جميع الأوقات إلا وقت منع مانع.",
     "en": "That is: you conceal at all times except the time when some impediment prevents [it]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الفاء لتفصيل المجمل كما في توضأ وغسل وجهه ويديه.",
     "en": "The fāʾ is for detailing what was stated in summary, as in “he performed ablution, and washed his face and his hands.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "وتأويل المفعول الأول بكل واحد بعيد.",
     "en": "And interpreting the first object as “each one [of them]” is far-fetched."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "مبني على أن تأويل المفعول الأول بكل واحد مما لا يعبأ به.",
     "en": "This is based on [the view] that interpreting the first object as “each one” is something not to be taken into account."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيه أن إعراب التثنية في الاسم الظاهر كإعراب الرفع والنصب والتذكير والتأنيث،",
     "en": "There is [an objection] to this: the inflection of the dual in the overt noun is like the inflection of the nominative and accusative, and [like] masculine and feminine;"},
    {"type": "pair",
     "ar": "فكما يجوز أن يتبدل الإعراب والتذكير والتأنيث عند الإعمالين يجوز أن يتبدل إعراب المثنى أيضا فيهما.",
     "en": "so just as the inflection, the masculine and the feminine may change under the two [alternative] governments, the inflection of the dual may likewise change under them."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لا يقال: لقائل أن يقول: لا يجوز أن يكون من باب إعمال الأول، وإلا لزم حمل كلامه على الوجه المرجوح، وهو حذف المفعول؛",
     "en": "It is not to be said: someone may say that it cannot belong to the category of making the first govern, for otherwise his speech would have to be taken in the less favored way, namely elision of the object;"},
    {"type": "pair",
     "ar": "لأنا نقول: الحذف لضرورة انكسار الوزن.",
     "en": "because we say: the elision is by necessity, [to avoid] breaking the metre."},
]
