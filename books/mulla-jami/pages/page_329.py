# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 329 (printed ٣٢٨)."""

PAGE_NUMBER = 329
PRINTED_PAGE = "٣٢٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فإن «التميمي» يدل دائما على أن لذات» at the foot of PDF p. 328.
    {"type": "matn",
     "ar": "ما نسبة إلى قبيلة تميم، و«ذو مال» يدل على أن ذاتا ما صاحب مال",
     "en": "…some essence there is a relation to the tribe of Tamīm, and “dhū māl” signifies that some essence is the possessor of wealth;"},
    {"type": "matn",
     "ar": "(أو خصوصا) أي: في بعض الاستعمالات بأن يدل في بعض المواضع على حصول معنى لذات ما، وحينئذ يجوز أن يقع نعتا، وفي بعضها لا يدل على ذلك، وحينئذ لا يصح جعله نعتا",
     "en": "(or specifically), that is, in some usages, in that in some places it signifies the presence of a meaning in some essence, and then it may occur as a qualifier, while in others it does not signify that, and then it is not sound to make it a qualifier,"},
    {"type": "matn",
     "ar": "(مثل: «مررت برجل أي رجل»[[١]]) أي: كامل في الرجولية،",
     "en": "(as in “I passed by a man—what a man!” (marartu bi-rajulin ayyi rajulin)), that is, perfect in manliness."},
    {"type": "matn",
     "ar": "فـ«أي رجل» باعتبار دلالته في مثل هذا التركيب على كمال الرجولية[[٢]] يصح أن يقع نعتا،",
     "en": "So “ayyu rajulin,” in view of its signifying, in such a construction, perfection of manliness, may soundly occur as a qualifier;"},
    {"type": "matn",
     "ar": "وفي مثل: «أي رجل عندك؟» لا يدل على هذا المعنى، فلا يصح أن يقع نعتا.",
     "en": "while in such as “Which man is with you?” it does not signify this meaning, so it cannot soundly occur as a qualifier."},
    {"type": "matn",
     "ar": "(و) مثل: مررت («بهذا الرجل»[[٣]]) فإن «هذا» يدل على ذات مبهمة، و«الرجل» على ذات معينة،",
     "en": "(And) as in: I passed (“by this man” (bi-hādhā l-rajul)); for “hādhā” signifies an indeterminate essence and “al-rajul” a specified essence,"},
    {"type": "matn",
     "ar": "وخصوصية الذات المعينة بمنزلة معنى حاصل في الذات المبهمة، فلهذا صح أن يقع «الرجل» صفة لـ«هذا»،",
     "en": "and the particularity of the specified essence stands in the place of a meaning present in the indeterminate essence; for this reason “al-rajul” may soundly occur as an adjective of “hādhā,”"},
    {"type": "matn",
     "ar": "وفي المواضع الأخر التي لا تدل على هذا المعنى لا يصح أن يقع صفة.",
     "en": "while in other places that do not signify this meaning it cannot soundly occur as an adjective."},
    {"type": "matn",
     "ar": "وذهب بعضهم إلى أن «الرجل» بدل عن اسم الإشارة، وبعضهم إلى أنه عطف بيان.",
     "en": "Some held that “al-rajul” is a substitute (badal) for the demonstrative noun, and some that it is an explicative apposition (ʿaṭf bayān)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: هذه تكون وصفا للنكرة، ومضافة إلى ما هو بمعناها،",
     "en": "That is, this [ayy] is a description of an indefinite noun and is annexed to what has its meaning."},
    {"type": "pair",
     "ar": "ويقرب منه كل وجد وحق تكون تابعة للجنس معرفة كان أو نكرة. وتكون مضافة إلى مثل متبوعها لفظا أو معنى،",
     "en": "Close to it are “kull,” “jidd” and “ḥaqq”: they follow a generic noun, whether definite or indefinite, and are annexed to the like of their qualified word, in wording or in meaning."},
    # REVIEW: «كان ما سواك هزل» and «كان من سواك باطل» are printed with the predicate of «كان» in the nominative form; transcribed as printed.
    {"type": "pair",
     "ar": "يقال: أنت الرجل كل الرجل، أي: أنه مجتمع فيه من خلال الخير ما تفرق في جميع الرجال وجد الرجل أي: كان ما سواك هزل وحق الرجل أي: كان من سواك باطل.",
     "en": "One says: “You are the man, all the man” (anta l-rajulu kullu l-rajuli), that is, there is gathered in him of good qualities what is dispersed among all men; and “the earnest of men” (jidd al-rajul), that is, what is other than you was jest; and “the true man” (ḥaqq al-rajul), that is, whoever is other than you was false."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بفتح الراء وضمها على ما في القاموس،",
     "en": "With fatḥa or ḍamma on the rāʾ (rajūliyya / rujūliyya), according to what is in al-Qāmūs."},
    {"type": "pair",
     "ar": "أي: إذا أضيف إلى لفظ موصوفه بعينه يكون مجازا عن الكمال في حقيقة دل عليها لفظ موصوفه. فالمراد بمثل هذا التركيب ذلك.",
     "en": "That is, when it is annexed to the very word of its qualified noun, it is a figure for perfection in the reality signified by the word of its qualified noun. This is what is meant by “such a construction.”"},
    {"type": "pair",
     "ar": "وقوله: وفي مثل أي رجل عندك لا يدل على هذا المعنى. فلا يصح أن يقع نعتا يرد عليه أنه ليس في هذا التركيب شيء يمكن أن يجعل موصوفا، حتى يظهر أن عدم الصحة من جانب أي رجل،",
     "en": "Against his words “while in such as ‘Which man is with you?’ it does not signify this meaning, so it cannot soundly occur as a qualifier,” the objection is raised that there is nothing in this construction that could be made the qualified noun, so that it would be clear that the unsoundness comes from the side of “ayyu rajulin.”"},
    {"type": "pair",
     "ar": "فالأولى أن يقال: وفي مثل مررت بضارب أي رجل لا يدل على هذا المعنى، فلا يصح أن يقع نعتا.",
     "en": "It would therefore be better to say: “while in such as ‘I passed by the striker of which man’ it does not signify this meaning, so it cannot soundly occur as a qualifier.”"},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "يعني: به اسم الجنس الجامد بالنظر إلى اسم الإشارة دون غيره، نحو: «مررت بزيد الرجل».",
     "en": "He means by it the non-derived generic noun (ism al-jins al-jāmid) in relation to the demonstrative noun, not to anything else, as in “I passed by Zayd the man.”"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: وذلك لأن استعمال الرجل بمعنى الكامل في الرجولية ليس وضعيا.",
     "en": "Shaykh al-Raḍī said: That is because the use of “al-rajul” in the sense of one perfect in manliness is not by coinage (waḍʿī)."},
    {"type": "pair",
     "ar": "ثم قال: إن قيل: لم لم يجز أن يوصف بأسماء الأجناس باقيا معناها على ما وضعت له سائر المبهمات كما يوصف بها أسماء الإشارة، فيقال: مررت بشخص رجل، وبسبع أسد كما يقال بهذا الرجل؟",
     "en": "Then he said: If it is said: why may the other indeterminate nouns not be qualified by generic nouns, their meaning remaining as coined, just as demonstrative nouns are qualified by them, so that one says “I passed by a person, a man” and “by a beast, a lion,” as one says “by this man”?"},
    {"type": "pair",
     "ar": "قلت: لتجرد الموصوف في مثله عن فائدة زائدة على ما كان يحصل من أسماء الأجناس، ولو لم يقع صفات؛",
     "en": "I say: because the qualified noun in such a case is devoid of any benefit beyond what would be obtained from the generic nouns even if they did not occur as adjectives;"},
    {"type": "pair",
     "ar": "إذ قولك: مررت برجل يفيد الشخصية. وأسد يفيد السبعية بخلاف رجل طويل؛ لأن الطول يكون في غير الرجل.",
     "en": "for your saying “I passed by a man” conveys personhood, and “lion” conveys being a beast of prey, unlike “a tall man,” since tallness occurs in other than a man."},
    {"type": "pair",
     "ar": "ولهذا يحذف الموصوف في الأغلب إذا كان مع قرينة دالة عليه كالغبراء والخضراء في الأرض والسماء.",
     "en": "For this reason the qualified noun is mostly elided when there is contextual evidence indicating it, as with “al-ghabrāʾ” (the dusty one) and “al-khaḍrāʾ” (the green one) for the earth and the sky."},
    {"type": "pair",
     "ar": "وأما قولك: هذا الرجل، فللموصوف فائدة جعل الوصف حاضرا.",
     "en": "As for your saying “this man,” the qualified noun has the benefit of making the description present."},
]
