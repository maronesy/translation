# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 435 (printed ٤٣٤)."""

PAGE_NUMBER = 435
PRINTED_PAGE = "٤٣٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… (أي: أحدها) لكن لا» at the foot of PDF p. 434 (mid-sentence).
    {"type": "matn",
     "ar": "مطلقا، بل باعتبار وقوعه في المرتبة الثالثة أو الرابعة أو الخامسة، وإلا يلزم[[١]] جواز إرادة الواحد الأول من عاشر العشرة[[٢]]، وذلك مستبعد جدا[[٣]].",
     "en": "…not absolutely, but with respect to its falling in the third, fourth or fifth rank; otherwise it would follow that “the first one” could be meant by “the tenth of ten”, and that is very far-fetched."},
    {"type": "matn",
     "ar": "(وتقول) في إضافة ما زاد على العشرة: (حادي عشر أحد عشر) بإضافة المركب الأول إلى المركب الثاني، أي: واحد من أحد عشر متأخر بعشر درجات بناء (على) الاعتبار (الثاني) وهو اعتبار بيان الحال (خاصة)؛",
     "en": "(And you say), in the annexation of what exceeds ten: (ḥādiya ʿashara aḥada ʿashara), by annexing the first compound to the second, that is, “one of eleven, coming ten degrees later”, built (on) the (second) consideration, which is the consideration of stating the condition, (exclusively);"},
    {"type": "matn",
     "ar": "لأن الاعتبار الأول لا يتجاوز العشرة كما عرفت.",
     "en": "because the first consideration does not go beyond ten, as you have learned."},
    {"type": "matn",
     "ar": "(وإن شئت قلت) في أداء هذا المعنى: (حادي أحد عشر) بحذف الجزء الأخير من المركب الأول استغناء عنه بذكره في المركب الثاني،",
     "en": "(And if you wish, you say), in expressing this meaning: (ḥādī aḥada ʿashara), by dropping the last part of the first compound, its mention in the second compound making it dispensable."},
    {"type": "matn",
     "ar": "وهكذا تقول: (إلى تاسع تسعة عشر فتعرب) الجزء (الأول[[٤]]) من المركب الأول؛ لانتفاء التركيب الموجب للبناء،",
     "en": "And so you say (up to tāsiʿu tisʿata ʿashara; so you inflect) the (first) part of the first compound, because the compounding that necessitates indeclinability (bināʾ) is absent;"},
    {"type": "matn",
     "ar": "وبني الجزآن الباقيان لوجود موجب البناء فيهما، وهو التركيب.",
     "en": "and the two remaining parts are indeclinable, because what necessitates indeclinability is present in them, namely compounding."},

    {"type": "section", "ar": "[المذكر والمؤنث]",
     "en": "The Masculine and the Feminine"},

    {"type": "matn",
     "ar": "(المذكر والمؤنث[[٥]]) ذكرهما بعد باب العدد؛ لانجرار مباحثه إلى ذكر التذكير والتأنيث،",
     "en": "(The masculine (mudhakkar) and the feminine (muʾannath)). He mentions them after the chapter on number because its discussions lead on to the mention of masculine and feminine gender."},
    {"type": "matn",
     "ar": "وقدم المذكر لأصالته[[٦]]، وأخر تعريفه؛ لأنه عدمي، وتعريف المؤنث وجودي.",
     "en": "He put the masculine first because it is the base, but put its definition last, because it is privative (ʿadamī), whereas the definition of the feminine is positive (wujūdī)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: إذا كان المراد الواحد مطلقا لا بخصوصية المرتبة يلزم جواز إرادة كل واحد سواء كان الأول أو الثاني أو الثالث من كل ما جاء للواحد من المتعدد باعتبار حاله،",
     "en": "That is, if what is meant were “one” absolutely, not in the particularity of the rank, it would follow that every one could be meant, whether the first, the second or the third, by everything that has come [as a name] for one of a multiple with respect to its condition."},
    {"type": "pair",
     "ar": "وتخصيص الشارح الواحد الأول وعاشر العشرة لغاية البعد بينهما.",
     "en": "The commentator singled out “the first one” and “the tenth of ten” because of the utmost distance between them."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يجوز إرادة المبدأ والمنتهى من عاشر العشرة؛ لأنهما في المرتبة العاشرة كل منهما باعتبار مبدأ،",
     "en": "Both the starting point and the end point may be meant by “the tenth of ten”, because each of them is in the tenth rank with respect to a starting point."},
    {"type": "pair",
     "ar": "فينبغي أن يقول: وإلا يلزم جواز إرادة الواحد الثاني والثالث مثلا.",
     "en": "So he should have said: “otherwise it would follow that the second and the third one, for example, could be meant.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: عند العقل؛ إذ الظاهر أن يقال: أول العشرة وثاني العشرة إلى عاشرها. وأما الاستعمال فغير واقع.",
     "en": "That is, to reason; for the obvious thing is to say “the first of the ten”, “the second of the ten”, up to “its tenth”. As for usage, it does not occur."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ويظهر الفرق بين الإعراب والبناء في اللفظ فيما ليس في آخره حرف علة، أو فيما آخره حرف علة في حال النصب،",
     "en": "The difference between inflection and indeclinability appears in the wording in what has no weak letter at its end, or, in what ends in a weak letter, in the accusative state;"},
    {"type": "pair",
     "ar": "فإنه في البناء ساكن الآخر وفي الإعراب ساكن الآخر أيضا إلا في حال النصب.",
     "en": "for in indeclinability its end is quiescent, and in inflection its end is also quiescent except in the accusative state."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: من الاسم المتمكن؛ لأن ما هو المبني منهما من أسماء الإشارات والموصولات والمضمرات سبق ذكره،",
     "en": "That is, of the fully declinable noun (al-ism al-mutamakkin); for what is indeclinable among the two, among the demonstratives, relatives and pronouns, has been treated already."},
    {"type": "pair",
     "ar": "فلا يرد أن نحو: هذي والتي وأنت خارج عن تعريف المؤنث داخل في تعريف المذكر، فينتقضان طردا وعكسا،",
     "en": "So it cannot be objected that the like of “hādhī”, “allatī” and “anti” falls outside the definition of the feminine and inside the definition of the masculine, so that both [definitions] are broken, as to exclusiveness and as to inclusiveness (ṭardan wa-ʿaksan)."},
    # REVIEW: printed «للمؤنت» (with tāʾ), evidently for «للمؤنث»; transcribed as printed.
    {"type": "pair",
     "ar": "وأحكام الإسناد الآتية إنما هي للمؤنت الذي هو قسم الاسم المتمكن،",
     "en": "The rules of predication (isnād) that follow belong only to the feminine that is a kind of the fully declinable noun;"},
    {"type": "pair",
     "ar": "فإن المؤنث من أسماء الإشارة والموصولات والمضمرات في تلك الأحكام تابع لما يعبر بها عنه في كونه حقيقيا أو غيره.",
     "en": "for the feminine among the demonstratives, relatives and pronouns follows, in those rules, what is expressed by them, as to whether it is real (ḥaqīqī) or otherwise."},
    {"type": "pair",
     "ar": "وكذا المثنى والمجموع المعرفان بما سيأتي أريد بهما ما هو قسم الاسم المتمكن، والأحكام المذكورة لهما فيما سيأتي أحكام لما هو قسم منه.",
     "en": "Likewise, the dual and the plural that are defined in what follows: what is meant by them is what is a kind of the fully declinable noun, and the rules stated for them in what follows are rules for what is a kind of it."},

    # ---------------- Footnote 6 (continues on PDF p. 436) ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إذ ما من مذكر ولا مؤنث إلا ويطلق عليه الشيء، والشيء مذكر،",
     "en": "For there is nothing masculine or feminine to which “thing” (shayʾ) is not applied, and “thing” is masculine;"},
    {"type": "pair",
     "ar": "ولأنه لا يفتقر إلى زيادة والتأنيث لا يحصل إلا بزيادة،",
     "en": "and because it needs no addition, whereas the feminine is produced only by an addition;"},
    {"type": "pair",
     "ar": "ولا يتحقق التذكير والتأنيث إلا في الأسماء إذا قصد مدلولاتها، فإن قصد لفظ",
     "en": "and masculine and feminine gender are realized only in nouns when their meanings are intended. If the word…"},
]
