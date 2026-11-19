# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 126 (printed ١٢٥)."""

PAGE_NUMBER = 126
PRINTED_PAGE = "١٢٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "الاسم في هذه الحالة منصرف، أو غير منصرف؟",
     "en": "Is the noun, in this state, fully inflected or not fully inflected?"},
    {"type": "matn",
     "ar": "فمنهم من ذهب إلى أنه منصرف مطلقا؛ لأن عدم انصرافه إنما كان لمشابهته الفعل، فلما ضعفت هذه المشابهة بدخول ما هو من خواص الاسم، أعني: اللام أو الإضافة[[١]]، قويت جهة الاسمية، فرجع إلى أصله الذي هو الصرف، فدخله الكسر دون التنوين؛ لأنه لا يجتمع مع اللام والإضافة.",
     "en": "Some held that it is fully inflected absolutely; because its non-inflection was only due to its resemblance to the verb, so when this resemblance was weakened by the entry of what belongs to the special properties of the noun — I mean the definite article (lām) or the genitive construction (iḍāfa) — the aspect of nounhood was strengthened, and it reverted to its base, which is full inflection. Thus the kasra entered it, but not the tanwīn, because [tanwīn] does not co-occur with the lām and the iḍāfa."},
    {"type": "matn",
     "ar": "ومنهم من ذهب إلى أنه غير منصرف مطلقا، والممنوع من غير المنصرف بالأصالة هو التنوين، وسقوط الكسر إنما هو بتبعية التنوين، وحيث ضعفت[[٢]] مشابهته للفعل لم تؤثر إلا في سقوط التنوين دون تابعه الذي هو الكسر، فعاد الكسر إلى حاله، وسقط التنوين لامتناعه من الصرف.",
     "en": "Some held that it is not fully inflected absolutely; and what is barred from the non-inflecting [noun] by original right is the tanwīn, while the dropping of the kasra is only by way of following the tanwīn. So when its resemblance to the verb was weakened, it had effect only in the dropping of the tanwīn, not of its dependent, which is the kasra; hence the kasra returned to its [original] state, and the tanwīn dropped on account of [the noun’s] being barred from full inflection."},
    {"type": "matn",
     "ar": "ومنهم من ذهب إلى أن العلتين إن كانتا باقيتين مع اللام أو الإضافة كان الاسم غير منصرف، وإن زالتا معا، أو زالت إحداهما كان منصرفا.",
     "en": "Some held that, if the two causes remain together with the lām or the iḍāfa, the noun is non-inflecting; but if both depart, or one of them departs, it is fully inflected."},
    {"type": "matn",
     "ar": "وبيان ذلك: أن العلمية تزول باللام أو الإضافة[[٣]]، فإن كانت العلمية شرطا للسبب الآخر زالتا معا، كما في «إبراهيم»، وإن لم يكن شرطا، كما في «أحمد» زالت إحداهما، وإن لم تكن هناك علمية، كما في «أحمر» بقيت العلتان على حالهما، وهذا القول أنسب بما عرف به المصنف غير المنصرف.",
     "en": "The clarification of this is that proper-nounhood departs through the lām or the iḍāfa. So if proper-nounhood is a condition for the other cause, both depart together, as in “Ibrāhīm”; if it is not a condition, as in “Aḥmad,” one of the two departs; and if there is no proper-nounhood there, as in “aḥmar,” the two causes remain as they are. This doctrine is the most fitting with the definition by which the author defined the non-inflecting [noun]."},

    {"type": "section", "ar": "[المرفوعات]", "en": "The Nominatives (al-Marfūʿāt)"},

    {"type": "matn",
     "ar": "(المرفوعات[[٤]]) جمع «المرفوع» لا «المرفوعة»[[٥]]؛ لأن موصوفه الاسم، وهو",
     "en": "(al-Marfūʿāt, “the nominatives”) is the plural of “al-marfūʿ” (masculine), not of “al-marfūʿa” (feminine), because that which it qualifies is the noun (ism), and it [is]…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "دون سائر الخواص كالفعلية والمفعولية. قيل: وجه ذلك أنهما مغيرتان لمدلول الاسم بخلاف البواقي.",
     "en": "As opposed to the other special properties, such as [being susceptible to] verbal government or objecthood. It is said: the reason for this is that these two (the lām and the iḍāfa) alter the signification of the noun, unlike the remaining [properties]."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيل في توجيه عدم سقوط الكسرة: إن التنوين كالثابت لوجود خلفه، وهو اللام أو الإضافة، أو أنه محذوف لا لمنع الصرف، بل للإضافة أو اللام.",
     "en": "It has been said, in justifying the non-dropping of the kasra: that the tanwīn is as though established, because of the presence of its substitute — namely the lām or the iḍāfa; or that it is elided not on account of the prevention of full inflection, but on account of the iḍāfa or the lām."},
    {"type": "pair",
     "ar": "وفيه انهم صرحوا بأن الإضافة في حواج بيت الله معاقبة للتنوين المقدر.",
     "en": "Against this stands that they explicitly stated, regarding the iḍāfa in “ḥawājja bayti-llāh” [pilgrims of the House of Allah], that it stands in alternation with the implied tanwīn."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فيه أن اللام تجامع العلمية إذا كان العلم في الأصل مصدرا أو صفة كالفضل والحسن.",
     "en": "Against this stands that the lām co-occurs with proper-nounhood when the proper name is originally a verbal noun or an adjective, such as “al-Faḍl” and “al-Ḥasan.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إنما جمع ولم يأت بالمفرد؛ لأن تعريف المرفوع وتعريف الرفع يوهمان أن المرفوع ليس إلا واحدا هو الفاعل، فأزال ذلك الوهم بصيغة الجمع الدالة على التعدد.",
     "en": "He used the plural and did not bring the singular, because the definition of “the nominative” and the definition of “nominative case” suggest that the nominative is but one, namely the agent (fāʿil); so he removed that misapprehension by the plural form, which signifies multiplicity."},
    {"type": "pair",
     "ar": "إلا أنها في المجرورات لمجرد المشاكلة، وفي المنصوبات مستعارة للكثرة، وههنا في موقعها.",
     "en": "Except that in [the term] “al-majrūrāt” (the genitives) it is merely for formal conformity, and in “al-manṣūbāt” (the accusatives) it is borrowed to indicate abundance; whereas here it is in its proper place."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لما ذهب الوهم من قاعدة تصرف صيغة اسم المفعول إلى أن يكون المرفوعات جمع مرفوعة لا مرفوع حكم بعكس ذلك لرفع ذلك التوهم.",
     "en": "Since one’s supposition might, from the rule of the free morphological variation of the passive-participle form, stray to [thinking] that “al-marfūʿāt” is the plural of “marfūʿa” (feminine) rather than “marfūʿ,” he ruled to the contrary of that so as to remove that misapprehension."},
]
