# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 85 (printed ٨٤)."""

PAGE_NUMBER = 85
PRINTED_PAGE = "٨٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "verse",
     "ar": "(عدل ووصف وتأنيث ومعرفة        وعجمة ثم جمع ثم تركيب)",
     "en": "Alteration (ʿadl), description (waṣf), femininity (taʾnīth), and definiteness (maʿrifa); / and foreignness (ʿujma), then plurality (jamʿ), then compounding (tarkīb)."},
    {"type": "matn",
     "ar": "والعدول في عطف هاتين العلتين[[١]] من الواو إلى (ثم)[[٢]] لمجرد المحافظة على الوزن.",
     "en": "The shift, in conjoining these two causes, from the wāw to “thumma” (then) is merely for the sake of preserving the metre."},
    {"type": "verse",
     "ar": "(والنون[[٣]] زائدة من قبلها ألف        ووزن فعل وهذا القول تقريب)",
     "en": "And the nūn is extra, before which is an alif; / and the pattern of a verb (wazn fiʿl) — and this statement is [only] an approximation (taqrīb)."},
    {"type": "matn",
     "ar": "فقوله: «زائدة» منصوب على أنه حال[[٤]]؛ إذ المعنى[[٥]]: ويمنع النون الصرف حال كونها زائدة.",
     "en": "His words “zāʾida” (extra) are in the accusative as a circumstantial qualifier (ḥāl); for the meaning is: the nūn prevents full inflection (ṣarf) while being extra."},
    {"type": "matn",
     "ar": "وقوله: «ألف»[[٦]] فاعل الظرف المتقدم، أعني: «من قبلها»، أو مبتدأ خبره الظرف المتقدم.",
     "en": "And his words “alif” are the subject (fāʿil) of the preceding adverbial phrase — namely, “before which” (min qablihā) — or a subject (mubtadaʾ) whose predicate is the preceding adverbial phrase."},
    {"type": "matn",
     "ar": "ولا يخفى أنه لا يفهم من هذا التوجيه زيادة الألف، مع أنها أيضا زائدة، ولهذا يعبر عنهما بالألف والنون الزائدتين، ولو جعل «الألف» فاعلا[[٧]] لقوله: «زائدة»[[٨]]،",
     "en": "It is not hidden that this construal does not convey the extra-ness of the alif, even though it too is extra — which is why they are referred to as “the extra alif and nūn”; and were “the alif” made the subject (fāʿil) of his words “zāʾida” (extra),"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "«ثم» للتراخي في الزمان. ويستعار للتراخي في الرتبة، فيكون ما بعده أعلى رتبة مما قبله أو أدنى.",
     "en": "“Thumma” [denotes] succession with an interval in time. It is also borrowed for succession in rank, so that what follows it is of higher rank than what precedes it, or lower."},
    {"type": "pair",
     "ar": "ولا يخفى أن الجمع أعلى مرتبة مما قبله ومما بعده. فكلمة «ثم» في العلتين لهذه النكتة الجليلة.",
     "en": "It is not hidden that plurality (al-jamʿ) is of higher rank than what precedes it and what follows it. So the word “thumma” between the two causes is for this lofty subtle point."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فجردت عن التراخي، وأريد مجرد المشاركة، وذلك لأن ثبوت العلية للجمع ليس متأخرا عن ثبوتها لما سبق، وكذا الحال في التركيب.",
     "en": "It was stripped of [the sense of] interval, and mere participation (musharaka) was intended; that is because the establishing of causality for the plural is not posterior to its establishing for what preceded — and likewise the case regarding compounding (al-tarkīb)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه مساهلة؛ إذ العلة مجموع الألف والنون.",
     "en": "In it is a looseness (musāhala), since the cause is the totality of the alif and the nūn [together]."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أو صفة موصوف محذوف، أو منصوب بتقدير «أعني»؛ لأن النون لما ذكرت مطلقة احتيج إلى تعيين المراد.",
     "en": "Or [it is] the adjective of an elided described noun; or accusative by an implied “aʿnī” (I mean), because since the nūn was mentioned unrestrictedly, specifying what is intended became necessary."},
    {"type": "pair",
     "ar": "ويجوز أن يكون مرفوعا على أنه صفة للنون؛ لأن اللام للعهد الذهني، زيدت للمحافظة على الوزن، يدل عليه تنكير الباقي، أو بدل بحذف موصوف، أي: نون زائدة، أو خبر مبتدأ محذوف، أي: هي زائدة، والجملة معترضة.",
     "en": "It may also be in the nominative as an adjective of “the nūn,” because the [definite] lām is for mental familiarity (al-ʿahd al-dhihnī) — having been added for preserving the metre, as is indicated by the indefiniteness of the rest; or [it is] a substitute (badal) with an elided described noun, i.e., “an extra nūn”; or the predicate of an elided subject, i.e., “it is extra,” the sentence being parenthetical."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وذلك لأن قوله: «عدل» إلى آخره تعداد للموانع؛ لأنه خبر مبتدأ محذوف أي: تلك التسع هذه، أو بدل من «تسع»، أو بيان لها، فالعامل هو المنع المفهوم من المقام من غير تقديره في نظم الكلام.",
     "en": "That is because his words “ʿadl…” to the end are an enumeration of the preventers [of full inflection]; for it is the predicate of an elided subject, i.e., “those are the nine”; or it is a substitute for “nine,” or an explication of it; so the governing operator is the prevention (al-manʿ) understood from the context, without its being posited in the sequence of the discourse."},
    {"type": "pair",
     "ar": "قيل: يجوز أن يكون عاملها التعريف المستفاد من اللام، كما قيل في قوله تعالى: {والأرض جميعا قبضته} (سورة الزمر: ٦٧).",
     "en": "It has been said: its operator may be the definiteness derived from the lām — as was said regarding His words, the Exalted: “And the whole earth will be within His grip” (Qurʾān, Sūrat al-Zumar 39:67)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الجملة حال من صاحب الحال الأولى، فيكون من الأحوال المترادفة، أو من ضميره المستتر في «زائدة»، فيكون من الأحوال المتداخلة، أو صفة.",
     "en": "The sentence is a circumstantial qualifier of the subject of the first ḥāl, so it would be among the consecutive (mutarādifa) ḥāls; or [a ḥāl] of its concealed pronoun in “zāʾida,” so it would be among the nested (mutadākhila) ḥāls; or [it is] an adjective."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الفرق بين ما بين ما إذا جعل ظرفا للزيادة، أو لنفس الزائد؛ إذ على الأول يفهم زيادتهما، وتقدم زيادة الأولى على الثانية، وعلى الثاني لا يفهم إلا تقدم الأولى بحسب الوضع على الثانية.",
     "en": "The difference between what has been explained [is]: whether it is made an adverbial [qualifier] of “the extra-ness” (al-ziyāda) or of the extra [element] itself (nafs al-zāʾid); for on the first, the extra-ness of both is understood, as is the precedence of the first’s extra-ness over the second’s; whereas on the second, only the precedence of the first over the second by [conventional] positioning (waḍʿ) is understood."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "هذا مما لا يقصد بالزيادة قبل شيء في عرف أرباب التأليف؛ إذ لا يقصد به إلا التقدم في الذكر، ففهمه في عبارتهم بعيد جدا.",
     "en": "This is among the cases in which “extra-ness before something” is not intended in the convention of authors; since nothing is meant by it except precedence in mention, so to understand it [otherwise] in their expression is very far-fetched."},
]
