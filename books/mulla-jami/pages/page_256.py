# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 256 (printed ٢٥٥)."""

PAGE_NUMBER = 256
PRINTED_PAGE = "٢٥٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أي: «تعترك العراك» و«ينفرد وحده»» from the foot of PDF p. 255.
    {"type": "matn",
     "ar": "أي: انفراده و«تجتهد جهدك»، فهذه الجمل الفعلية وقعت حالا[[١]]، وهذه المصادر منصوبة على المصدرية.",
     "en": "…that is, “his being alone,” and “you exert your utmost exertion”; so these verbal clauses occur as a ḥāl, and these maṣdars are in the accusative as verbal nouns (maṣdariyya)."},
    {"type": "matn",
     "ar": "وثانيهما: أنها معارف موضوعة موضع النكرات[[٢]]، أي: معتركة ومنفردا ومجتهدا،",
     "en": "The second: that they are definites placed in the position of indefinites, that is, “jostling,” “alone” and “exerting oneself”;"},
    {"type": "matn",
     "ar": "فالصورة وإن كانت معرفة فهي في التقدير نكرة، كما أن «حسن الوجه» في صورة المعرفة، وهي في المعنى نكرة.",
     "en": "so the form, though definite, is indefinite in its underlying construal, just as “ḥasan al-wajh” (handsome of face) has the form of a definite while being indefinite in meaning."},
    {"type": "matn",
     "ar": "(فإن كان صاحبها) أي: صاحب الحال[[٣]] (نكرة[[٤]] محضة) لم يكن فيها شائبة تخصيص بما سوى التقديم،",
     "en": "(If its owner), that is, the owner of the ḥāl, (is a pure indefinite), having no trace of specification by anything other than preposing,"},
    {"type": "matn",
     "ar": "ولم تكن الحال مشتركة[[٥]] بينها وبين المعرفة نحو: «جاءني رجل وزيد راكبين»",
     "en": "and the ḥāl is not shared between it and a definite, as in “A man and Zayd came to me, both riding,”"},
    {"type": "matn",
     "ar": "(وجب تقديمها) أي: تقديم الحال على صاحبها،",
     "en": "(its preposing is obligatory), that is, preposing the ḥāl before its owner,"},
    {"type": "matn",
     "ar": "ليتخصص[[٦]] النكرة بتقديمها؛ لأنهما في المعنى مبتدأ وخبر[[٧]]،",
     "en": "so that the indefinite becomes specified by its preposing, because the two are in meaning a mubtadaʾ and a khabar;"},
    {"type": "matn",
     "ar": "ولئلا يلتبس بالصفة في النصب[[٨]] في مثل قولنا: «ضربت رجلا راكبا»، ثم قدمت في سائر المواضع وإن لم يلتبس؛ طردا للباب.",
     "en": "and so that it is not confused with an adjective in the accusative, in an example such as our saying “I struck a riding man”; then it was preposed in all other places, even where there is no confusion, for the consistency of the rule (ṭardan li-l-bāb)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الظاهر أحوالا.",
     "en": "The apparent [wording] would be “aḥwālan” (as ḥāls)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "هذا هو الوجه المرجح الذي يليق أن يكتفى به بجريانه في الأحوال المعرفة كلها بخلاف الأول، فإنه لا يجري إلا في المصادر.",
     "en": "This is the preferred way, fit to be relied on alone, since it applies to all definite ḥāls, unlike the first, which applies only to maṣdars."},
    {"type": "pair",
     "ar": "قال عبد الغفور: يعني: أن اللام للعهد الذهني أو زائدة.",
     "en": "ʿAbd al-Ghafūr said: he means that the lām is for mental definite reference (al-ʿahd al-dhihnī), or is redundant."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: المفردة؛ إذ الجملة لا يجب فيها التقديم بل الواحد من الضمير والواو وكلاهما.",
     "en": "He means the single-word [ḥāl]; for with a clause preposing is not obligatory, but rather one of the [linking] pronoun and the wāw, or both."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "والحال مفردا؛ إذ لو كانت جملة لوجب الواو لا التقديم.",
     "en": "With the ḥāl being a single word; for if it were a clause, the wāw would be obligatory, not preposing."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "الحال المشتركة صاحبها مجموع المعرفة والنكرة، ومجموع المعرفة والنكرة ليست بمعرفة ولا نكرة، نحو: «جاءني رجل وزيد راكبين».",
     "en": "The owner of a shared ḥāl is the definite and the indefinite taken together, and the definite and indefinite taken together are neither definite nor indefinite, as in “A man and Zayd came to me, both riding.”"},
    {"type": "pair",
     "ar": "فبقوله: «نكرة» يخرج صاحب الحال المشتركة. ولا حاجة إلى زيادة قيد. ولم يكن الحال مشتركة بينها وبين معرفة.",
     "en": "So by his word “indefinite” the owner of a shared ḥāl is excluded, and there is no need for the added qualification “and the ḥāl is not shared between it and a definite.”"},
    # REVIEW: print reads «فإنه لأضيافنا» (sense unclear; perhaps «فإنه لا ضيافنا» or a misprint); transcribed as printed.
    {"type": "pair",
     "ar": "ومن هذا يظهر وجه بديع لتقييد تعريف صاحب الحال بكونه غالبا، فاحفظه، فإنه لأضيافنا.",
     "en": "From this there appears a fine reason for qualifying the definiteness of the owner of the ḥāl as being “for the most part”; so retain it, for it is for our guests [sic]."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "فيه أن الحال إما عن الفاعل، أو عن المفعول به، وكل منهما مختص بالحكم المتقدم، فلا حاجة إلى تخصيص آخر،",
     "en": "Against this: the ḥāl is either of the agent or of the direct object, and each of them is already specified by the preceding judgement, so there is no need for further specification;"},
    {"type": "pair",
     "ar": "اللهم إلا أن يقال: الحال حكم آخر فلا يجدي التخصيص الحاصل بالقياس إلى حكم آخر.",
     "en": "unless it be said that the ḥāl is a further judgement, so a specification obtained with respect to another judgement is of no avail."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "فيه أن «جاء قائما رجل» في الحقيقة «قائم رجل»، فالتخصيص بالخبر المقدم الذي ليس بظرف، وهو لا ينفع في تصحيح الابتداء",
     "en": "Against this: “There came, standing, a man” is in reality “standing [is] a man,” so the specification is by a preposed predicate that is not an adverbial, and that is of no use in validating [an indefinite as] the mubtadaʾ."},
    {"type": "pair",
     "ar": "لا تقول: الحال بمنزلة الظرف، فتقديمه كتقديم الخبر الظرف؛ لأنا نقول: لا يصح الإخبار عن الجثة بظرف الزمان.",
     "en": "Do not say: the ḥāl has the status of an adverbial, so preposing it is like preposing an adverbial predicate; for we say: predicating an adverbial of time of a concrete entity (juththa) is not valid."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "ينبغي ألا يقيد تخصيص ذي الحال بالإضافة إلى النكرة ولا بصفة ولا باستغراق،",
     "en": "The specification of the owner of the ḥāl ought not to be restricted to annexation to an indefinite, nor to an adjective, nor to all-inclusiveness,"},
    {"type": "pair",
     "ar": "نحو: رأيت غلام رجل راكبا، ورأيت رجلا عالما راكبا، ونحو: ما رأيت رجلا راكبا؛ لأن الالتباس بالصفة باق بعد.",
     "en": "as in “I saw a man’s servant riding,” “I saw a learned man riding,” and “I did not see a man riding”; because confusion with an adjective still remains."},
]
