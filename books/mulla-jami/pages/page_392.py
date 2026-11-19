# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 392 (printed ٣٩١)."""

PAGE_NUMBER = 392
PRINTED_PAGE = "٣٩١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Follows «(و«فعال») حال كونه (مصدرا معرفة، كـ«فجار») بمعنى: الفجرة أو الفجور.» at the foot of PDF p. 391 (new sentence).
    {"type": "matn",
     "ar": "قال الشارح الرضي[[١]]: هو على ما قيل مصدر معرفة مؤنث، ولم يقم لي إلى الآن دليل قاطع على تعريفه ولا تأنيثه.",
     "en": "The commentator al-Raḍī said: it is, according to what has been said, a definite feminine maṣdar; but no decisive proof of its definiteness or of its femininity has yet been established for me."},
    {"type": "matn",
     "ar": "(و) حال كونه (صفة) لمؤنث[[٢]] (مثل: «يا فساق») بمعنى: «يا فاسقة»",
     "en": "(And) when it is (a qualifier) of a feminine, (as in “yā fasāqi”), in the sense of “yā fāsiqatu” (O wicked woman):"},
    {"type": "matn",
     "ar": "(مبني) أي: كل واحد من القسمين الأخيرين مبني (لمشابهته له) أي: لـ«فعال» بمعنى الأمر (عدلا وزنة)",
     "en": "(it is indeclinable), that is, each of the last two kinds is indeclinable, (because it resembles it), that is, “faʿāli” in the sense of the imperative, (in diversion (ʿadl) and in measure)."},
    # REVIEW: a full stop is printed before «أما» («وزنة) .أما زنة»); placed after the parenthesis here.
    {"type": "matn",
     "ar": "أما زنة، فظاهر. وأما عدلا[[٣]]، فلما ذهب إليه النحاة أن «فعال» بمعنى الأمر معدول عن الأمر الفعلي للمبالغة،",
     "en": "As for measure, it is evident. As for diversion, it is because of what the grammarians held: that “faʿāli” in the sense of the imperative is diverted from the verbal imperative for intensity,"},
    {"type": "matn",
     "ar": "وهذه الصيغة للمبالغة في الأمر، كـ«فعال وفعول» للمبالغة في الفاعل.",
     "en": "this form being for intensity in the imperative, as “faʿʿāl” and “faʿūl” are for intensity in the agent."},
    {"type": "matn",
     "ar": "قال الشارح الرضي: والذي أرى أن كون أسماء الأفعال معدولة عن ألفاظ الفعل شيء لا دليل لهم عليه،",
     "en": "The commentator al-Raḍī said: what I hold is that the verbal nouns’ being diverted from the expressions of the verb is something for which they have no proof."},
    {"type": "matn",
     "ar": "كيف والأصل في كل معدول عن شيء ألا يخرج عن النوع الذي ذلك الشيء منه[[٤]]؟ فكيف يخرج الفعل بالعدل من الفعلية إلى الاسمية؟",
     "en": "How could it be, when the rule for everything diverted from something is that it does not leave the kind to which that thing belongs? So how would the verb pass by diversion from verbhood to nounhood?"},
    {"type": "matn",
     "ar": "وأما المبالغة، فهي ثابتة في جميع أسماء الأفعال. وبين وجهها في كلام طويل، فمن أراد الاطلاع عليه، فليرجع إليه.",
     "en": "As for intensity, it is present in all verbal nouns. He explained the reason for it at length; whoever wishes to learn of it should refer to it."},
    {"type": "matn",
     "ar": "(و«فعال») حال كونه (علما للأعيان[[٥]]) أي: لعين من الأعيان، وإنما قال: علما",
     "en": "(And “faʿāli”) when it is (a proper name for concrete things), that is, for one concrete thing among others. He said “a proper name”…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وقال أيضا: إن من كان مذهبه أن جميع أوزان فعال أمرا، أو صفة، أو مصدرا، أو علما مؤنثة، فإذا سمي بها مذكر وجب عدم انصرافها كعناق.",
     "en": "He also said: whoever holds that all the forms of faʿāl—imperative, qualifier, maṣdar or proper name—are feminine, [for him,] when a male is named by one of them, it must be diptote, like ʿanāq."},
    {"type": "pair",
     "ar": "ويجوز عند النحاة جعلها منصرفة. وهذا منهم دليل على ترددهم في كونها مؤنثة.",
     "en": "Yet the grammarians allow making it fully declinable; and this on their part shows their hesitation over its being feminine."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لم يجيء في المذكر. وجميعها تستعمل من دون موصوف.",
     "en": "It does not occur for the masculine. All of them are used without a qualified noun."},
    {"type": "pair",
     "ar": "ويستعمل إما لازمة للنداء سماعا، نحو: يا فساق، وأما غير لازمة له،",
     "en": "It is used either as bound to the vocative, by attested usage, as in “yā fasāqi”, or as not bound to it."},
    {"type": "pair",
     "ar": "وهي على ضربين: أحدهما: ما صار بالغلبة علما جنسيا نحو: جباذ للمنية، وهي في الأصل لكل ما يجبذ أي: يجذب، ثم اختصت بالغلبة بجنس المنايا،",
     "en": "The latter is of two kinds. The first is what has become, by predominant usage, a generic proper name, as “jabādhi” for death: originally it was for everything that yajbidhu, that is, draws, and then by predominant usage it became restricted to the genus of deaths."},
    {"type": "pair",
     "ar": "والضرب الثاني ما بقي على وصفيتها نحو: قطاط أي: قاطة كافية.",
     "en": "The second kind is what has remained a qualifier, as “qaṭāṭi”, that is, “sufficient”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "إنما اعتبر ذلك؛ لأن الزنة غير كافية، وإلا لزم بناء سلام وكلام.",
     "en": "He took this into account only because measure is not sufficient; otherwise salām and kalām would have to be indeclinable."},
    {"type": "pair",
     "ar": "لكن فيه أن لا دليل على العدل، وثبوت الفجور وثبوت فاسقة لا يدلان على كون فجار وفساق معدولين عنهما لجواز أن يكونا مرادفين لهما.",
     "en": "But against this, there is no proof of diversion; the existence of fujūr and of fāsiqa does not show that fajāri and fasāqi are diverted from them, since they may be synonyms of them."},
    {"type": "pair",
     "ar": "وإن ادعى أن العدل مقدر لاضطرار وجودهما مبنيين كما في منع الصرف، قلنا: لا دليل على كون نزال معدولا عن انزل، وما استدلوا به عليه في غاية الضعف،",
     "en": "If it is claimed that diversion is supposed because their occurring as indeclinable compels it, as in diptosy, we say: there is no proof that nazāli is diverted from inzil, and what they have adduced for it is extremely weak."},
    {"type": "pair",
     "ar": "فالأولى أن يقال ما قاله الشيخ الرضي، وهو أن قسم المصادر والصفات بني لمشابهته لفعال الأمري زنة ومبالغة؛ إذ في الكل مبالغة.",
     "en": "So it is better to say what Shaykh al-Raḍī said: the class of maṣdars and qualifiers is indeclinable because it resembles the imperative faʿāli in measure and in intensity, since there is intensity in all of them."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يرد عليه أن ثلاث عدل عن ثلاثة ثلاثة، وثلاثة ثلاثة بتمامها ليست اسما، بل لفظا مركبا من اسمين، وخرج على التركيب إلى الاسمية",
     "en": "Against him it is objected that thulāth is diverted from thalātha thalātha (three by three), and thalātha thalātha as a whole is not a noun but an expression compounded of two nouns, and it passed out of compounding into nounhood;"},
    {"type": "pair",
     "ar": "إلا أن يقال: المراد أن الأصل ألا يخرج عن نوع أصله، أو نوع ما التأم منه أصله.",
     "en": "unless it be said: what is meant is that the rule is that it does not leave the kind of its origin, or the kind of that from which its origin is composed."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "حال من مفهوم قوله: مبني في الحجاز معرب في تميم أي: اختلف فيه حال كونه علما للأعيان.",
     "en": "A ḥāl from what is understood from his words “indeclinable in the Ḥijāz, declinable among Tamīm”, that is, “there is disagreement about it when it is a proper name for concrete things”."},
    {"type": "pair",
     "ar": "قلنا ذلك لأنه إن تعلق بكل من قوله: مبني ومعرب لزم توارد العاملين على معمول واحد،",
     "en": "We said this because, if it were attached to each of his words “indeclinable” and “declinable”, two governors would converge on one governed word;"},
    {"type": "pair",
     "ar": "وإن تعلق بأحدهما لزم خلو الآخر عن التعلق بهذا الحال، اللهم إلا أن يقدر للآخر كما في باب التنازع.",
     "en": "and if it were attached to one of them, the other would be left without connection to this ḥāl—unless it be supposed for the other, as in the chapter of contention (tanāzuʿ)."},
]
