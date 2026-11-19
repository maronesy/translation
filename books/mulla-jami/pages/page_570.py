# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 570 (printed ٥٦٩)."""

PAGE_NUMBER = 570
PRINTED_PAGE = "٥٦٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(فالأربعة الأول[[١]] للجمع[[٢]]) أي: جمع المعطوف والمعطوف عليه في حكم واحد، وهو أعم من أن يكون مطلقا[[٣]] أو مع ترتيب.",
     "en": "(So the first four are for conjunction (jamʿ)), that is, joining the coordinated term and that upon which it is coordinated in a single judgement, whether without qualification or with sequence (tartīb)."},
    # REVIEW: printed «أو وأما» (wa-ammā, with fatḥa and shadda) where the coordinating «إما» is meant; transcribed as printed (without diacritics).
    {"type": "matn",
     "ar": "ومراد النحاة بالجمع ههنا: ألا يكون لأحد الشيئين أو الأشياء كما كانت «أو وأما»،",
     "en": "What the grammarians mean by conjunction here is that [the judgement] not belong to one of the two things, or of the several things, as is the case with “aw” and “immā” [printed “ammā”];"},
    {"type": "matn",
     "ar": "وليس المراد اجتماع المعطوف[[٤]] والمعطوف عليه في الفعل في زمان أو مكان.",
     "en": "it does not mean the coming together of the coordinated term and that upon which it is coordinated in the action at one time or place."},
    {"type": "matn",
     "ar": "فقولك: «جاءني زيد، وعمرو، أو فعمرو، أو ثم عمرو»، أي: حصل الفعل من كليهما، لا من أحدهما دون الآخر.",
     "en": "So your saying “Zayd came to me, and ʿAmr”, or “… then ʿAmr (fa-ʿAmrun)”, or “… then later ʿAmr (thumma ʿAmrun)” means that the action came about from both of them, not from one of them to the exclusion of the other."},
    {"type": "matn",
     "ar": "(فالواو للجمع مطلقا لا ترتيب فيها) فقوله: «لا ترتيب فيها» بيان لإطلاقها،",
     "en": "(So wa is for conjunction without qualification; there is no sequence in it). His words “there is no sequence in it” explain its being unqualified,"},
    {"type": "matn",
     "ar": "أي: لا ترتيب فيها بين المعطوف والمعطوف عليه؛ بمعنى أنه لا يفهم هذا الترتيب منها وجودا وعدما.",
     "en": "that is, there is no sequence in it between the coordinated term and that upon which it is coordinated, in the sense that such a sequence is not understood from it, either as present or as absent."},
    {"type": "matn",
     "ar": "(والفاء للترتيب) أي: للجمع مع الترتيب بغير مهلة[[٥]].",
     "en": "(And fa is for sequence), that is, for conjunction with sequence without delay (muhla)."},
    {"type": "matn",
     "ar": "(و«ثم» مثلها) أي: مثل الفاء في مطلق الترتيب مقرونة (بمهلة[[٦]]).",
     "en": "(And “thumma” is like it), that is, like fa in sequence as such, joined (with delay)."},
    {"type": "matn",
     "ar": "(و«حتى» مثلها) أي: مثل «ثم» في الترتيب بمهلة، غير أن المهلة في حتى أقل منها في «ثم»، فهي متوسطة بين الفاء التي لا مهلة فيها وبين «ثم» المفيدة للمهلة.",
     "en": "(And “ḥattā” is like it), that is, like “thumma” in sequence with delay, except that the delay in ḥattā is less than in “thumma”; so it stands midway between fa, which has no delay, and “thumma”, which conveys delay."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فالفاء للتفسير، أي: الحروف العشرة بعد اشتراكها في التشريك ثلاثة أقسام بالحصول الحكمي:",
     "en": "The fa is explicative; that is, the ten particles, after sharing in making [two terms] partners (tashrīk), fall into three classes as regards the attainment of the judgement:"},
    {"type": "pair",
     "ar": "قسم يثبت به الحكم للتابع والمتبوع جميعا، وهي الأربعة الأول.",
     "en": "a class by which the judgement is established for the follower (tābiʿ) and the followed (matbūʿ) together, namely the first four;"},
    {"type": "pair",
     "ar": "وقسم يثبت به الحكم لأحدهما لا بعينه وهو أو وإما.",
     "en": "a class by which the judgement is established for one of the two, not a specific one, namely aw and immā;"},
    {"type": "pair",
     "ar": "وقسم يثبت به الحكم لأحدهما بعينه، وهو لا وبل ولكن.",
     "en": "and a class by which the judgement is established for a specific one of the two, namely lā, bal and lākin."},
    {"type": "pair",
     "ar": "ثم إن آحاد كل قسم تقترن باختصاص كل منهما بمعنى لا يوجد في الآخر.",
     "en": "Further, the individual members of each class are each marked by a meaning peculiar to it that is not found in the other."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     # REVIEW: elliptical; the English adds a bracketed "[not]" to make sense of it — this inserted negation reverses the literal wording and needs checking.
     "ar": "فالمعنى لإفادة الجمع؛ لأن موضوعها الجمع؛ لأنه ليس إلا موضوع الواو، وجزء من موضوعات البواقي.",
     "en": "So the meaning is: for conveying conjunction, [not] that what they are coined for is conjunction; for that is only what wa is coined for, and is part of what the others are coined for."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: لا يفهم منه الترتيب، أو يفهم منه الترتيب، فالأربعة للتشريك في مطلق الجمع، والواو للجمع المطلق.",
     "en": "That is, whether sequence is not understood from it or sequence is understood from it; so the four are for sharing in conjunction as such (muṭlaq al-jamʿ), while wa is for unqualified conjunction (al-jamʿ al-muṭlaq)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "ولا اجتماعهما في كونهما مقصودين بالنسبة لاستواء الجميع في ذلك.",
     "en": "Nor their coming together in both being intended by the predication, since all [ten] are alike in that."},
    {"type": "pair",
     "ar": "وقوله: في الفعل الأولى فيه أي: في الحكم ليشمل زيد وعمرو إنسانان.",
     "en": "As for his words “in the action”, it would be better [to say] instead “in the judgement”, so as to include “Zayd and ʿAmr are two human beings”."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: بشرط عدم المهلة، فإنه المتبادر عند الإطلاق؛ لأنه الكامل، فلا حاجة إلى التصريح.",
     "en": "That is, on condition of the absence of delay; for that is what comes first to mind when [sequence] is stated without qualification, since it is the complete [form], so there is no need to state it explicitly."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: printed «بلا مهملة» (muhmala); the sense requires «مهلة» (delay); transcribed as printed.
    {"type": "pair",
     "ar": "اعلم أن الفاء وثم قد يصلحان لتركيب واحد بأن يكون المعطوف أمرا ممتدا كان انتهاؤه متراخيا عن المعطوف عليه، وابتداؤه عقيبه بلا مهملة،",
     "en": "Know that fa and thumma may both suit a single construction, when the coordinated term is an extended matter whose end is delayed after that upon which it is coordinated, while its beginning follows immediately upon it without delay [printed “muhmala”];"},
    {"type": "pair",
     "ar": "فلك أن تعطف بالفاء نظرا إلى اتصال ابتدائه بالمعطوف عليه، وأن تعطف بـ«ثم» نظرا إلى بعد انتهائه وتراخيه عنه.",
     "en": "so you may coordinate with fa in view of the contiguity of its beginning with that upon which it is coordinated, and you may coordinate with “thumma” in view of the remoteness and delay of its end from it."},
]
