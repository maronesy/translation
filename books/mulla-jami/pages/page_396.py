# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 396 (printed ٣٩٥)."""

PAGE_NUMBER = 396
PRINTED_PAGE = "٣٩٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «(كل اسم) حاصل (من) تركيب» at the foot of PDF p. 395.
    {"type": "matn",
     "ar": "(كلمتين) حقيقة أو حكما[[١]]، اسمين أو فعلين[[٢]] أو حرفين أو مختلفين، وجعلهما كلمة واحدة (ليس بينهما نسبة) أصلا[[٣]] لا في الحال[[٤]] ولا قبل التركيب[[٥]].",
     "en": "…of (two words), really or by status, two nouns, two verbs, two particles, or of different kinds, and the making of them into one word, (between which there is no relation) at all, neither at present nor before the combination."},
    {"type": "matn",
     "ar": "وإنما قلنا: «حقيقة أو حكما» لئلا يخرج مثل: «سيبويه»[[٦]]، فإن الجزء الأخير منه صوت غير موضوع لمعنى، فلا تكون كلمة، لكنه في حكم الكلمة حيث أجرى مجرى الأسماء المبنية.",
     "en": "We said “really or by status” only so that the like of “Sībawayhi” would not be excluded: its last part is a sound not coined for a meaning, so it is not a word, but it has the status of a word, since it is treated like the indeclinable nouns."},
    {"type": "matn",
     "ar": "وقوله: «ليس بينهما نسبة» ليخرج مثل: «عبد الله[[٧]]، وتأبط شرا»؛ لأن بين جزئي كل واحد منهما نسبة قبل العلمية[[٨]].",
     "en": "His words “between which there is no relation” are to exclude the like of “ʿAbd Allāh” and “Taʾabbaṭa Sharran”, because between the two parts of each of them there was a relation before they became proper names."},
    {"type": "matn",
     "ar": "ولا يخفى أنه يخرج بهذا القيد مثل: «خمسة عشر» عن الحد مع أنه من أفراد المحدود؛ لأن بين جزئيه قبل التركيب نسبة العطف،",
     "en": "It is clear that this restriction excludes the like of “khamsata ʿashara” (fifteen) from the definition, although it is among the members of the thing defined, because between its two parts before the combination there is the relation of coordination (ʿaṭf);"},
    {"type": "matn",
     "ar": "وتعيين النسبة على وجه يخرج منها هذه النسبة أصعب من خرط القتاد[[٩]]،",
     "en": "and specifying the relation in a way that excludes this relation from it is harder than stripping the tragacanth thorn-bush by hand."},
    {"type": "matn",
     "ar": "والأحسن أن يقال[[١٠]]: المراد بالنسبة نسبة مفهومية من ظاهر هيئة تركيب إحدى الكلمتين مع الأخرى،",
     "en": "It is better to say: what is meant by “relation” is a relation understood from the outward form of the combination of one of the two words with the other;"},
    {"type": "matn",
     "ar": "ولا شك أنه يفهم من ظاهر الهيئة التركيبية التي في «عبد الله» النسبة الإضافية،",
     "en": "and there is no doubt that from the outward combinatory form in “ʿAbd Allāh” the genitive (iḍāfa) relation is understood,…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "ما وجد من هذه الأقسام التركيب من اسمين حقيقة نحو: بعلبك، أو حكما نحو: سيبويه، ومن اسم وفعل نحو: بخت نصر،",
     "en": "What is found among these kinds is combination of two nouns, really, as “Baʿlabakk”, or by status, as “Sībawayhi”; and of a noun and a verb, as “Bukhtanaṣṣar”;"},
    # REVIEW: «ونصر ماضي التفضيل» as printed; one would expect «التفعيل» (naṣṣara is a past of the faʿʿala/tafʿīl pattern). Transcribed as printed.
    {"type": "pair",
     "ar": "فإنه مركب من بخت بالضم، وهو معرب بوخت بمعنى الابن وجد عنده صنم اسمه نصر، فنسب إليه خرب بيت المقدس على ما في القاموس، ونصر ماضي التفضيل.",
     "en": "for it is compounded of “bukht”, with ḍamma, which is the Arabicized form of “būkht”, meaning “son”: he was found beside an idol named Naṣr, so he was ascribed to it; he destroyed Jerusalem (Bayt al-Maqdis), according to al-Qāmūs; and “naṣṣar” is a past tense of the pattern “al-tafḍīl” [as printed]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الموجود في هذه الأقسام هو المركب من الاسمين كبعلبك، أو من فعل واسم كبخت نصر.",
     "en": "What is found among these kinds is the compound of two nouns, as Baʿlabakk, or of a verb and a noun, as Bukhtanaṣṣar."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأنها نكرة في سياق النفي، فتعم.",
     "en": "Because it is an indefinite in a negative context, so it is general."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: في حال التركيب.",
     "en": "That is, in the state of combination."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "رد لبيان الرضي حيث قال: أي: ليس بينهما نسبة قبل العلمية.",
     "en": "A rejection of al-Raḍī’s explanation, where he said: that is, there was no relation between them before they became a proper name."},
    {"type": "pair",
     "ar": "ووجه الرد أنه عدول عن عموم العبارة بلا داع، لكنه ليس بذاك؛ لأن الاسم مستغن عن الوصف والتقييد بانتفاء النسبة في الحال،",
     "en": "The ground of the rejection is that it departs from the generality of the wording without cause. But that is not sound, because the noun has no need of being qualified and restricted by the absence of relation at present;"},
    {"type": "pair",
     "ar": "فالحاجة إلى التقييد بانتفاء النسبة قبل الاسمية، فحمله على العموم يوجب اعتبار ما لا يحتاج إليه في التعريف،",
     "en": "the need is only for restriction by the absence of relation before nounhood; so taking it as general requires considering what is not needed in the definition."},
    {"type": "pair",
     "ar": "نعم قوله: قبل التركيب أحسن من قوله: قبل العلمية لشموله: خمسة عشر.",
     "en": "Yes, his words “before the combination” are better than his [al-Raḍī’s] words “before becoming a proper name”, because they include “khamsata ʿashara”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فإنه من المركبات المبنيات للتركيب.",
     "en": "For it is among the compounds that are indeclinable because of combination."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لأنهما ليسا مبنيين للتركيب. أما الأول: فظاهر.",
     "en": "Because the two are not indeclinable because of combination. As for the first, it is evident."},
    {"type": "pair",
     "ar": "وأما الثاني: فلأنه قبل النقل جملة فليس بمعرب ولا مبني، وبعد النقل محكي على ما كان عليه.",
     "en": "As for the second, it is because before the transfer it is a sentence, and so is neither declinable nor indeclinable, and after the transfer it is reported as it was."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "إما حال التركيب أو قبل التركيب.",
     "en": "Either in the state of combination or before the combination."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "لأن النكرة الواقعة في سياق النفي صريحة في الاستغراق، فإرادة بعض الأفراد دون بعض من غير قرينة ترجيح بلا مرجح.",
     "en": "Because an indefinite occurring in a negative context is explicit in all-inclusiveness (istighrāq); so to intend some members to the exclusion of others without a contextual indication is preference without a preferring factor."},
    {"type": "pair",
     "ar": "وفيه تعريض بالفاضل الهندي حيث عين النسبة، فقال: ليس بينهما نسبة إسناد ولا إضافة ولا عمل ولا إفادة معنى.",
     "en": "In this there is an allusion to al-Fāḍil al-Hindī, since he specified the relation and said: between them there is no relation of predication (isnād), of annexation (iḍāfa), of government (ʿamal), or of conveying a meaning."},
    {"type": "pair",
     "ar": "فيخرج مثل: تأبط شرا وعبد الله ويزيد والنجم أعلاما.",
     "en": "So the like of Taʾabbaṭa Sharran, ʿAbd Allāh, Yazīd and al-Najm as proper names is excluded."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: الأحسن أن يفسر النسبة بحيث لا يدخل فيها هذه النسبة لا تعيينها ولا تخصيصها بأنه المراد نسبة مفهومة إلى آخره.",
     "en": "That is, it is better to interpret the relation such that this relation does not enter into it, not to specify it or particularize it by saying that what is meant is an understood relation, and so on."},
    {"type": "pair",
     "ar": "كما هو المتبادر أي: ليس ألا يكون بين الكلمتين نسبة في الواقع بل في اللفظ.",
     "en": "As is what first comes to mind; that is, it is not that there is no relation between the two words in reality, but rather in the wording."},
]
