# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 150 (printed ١٤٩)."""

PAGE_NUMBER = 150
PRINTED_PAGE = "١٤٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "لزم كونه مسندا ومسندا إليه معا، مع كون كل من الإسنادين تاما،",
     "en": "…it would follow that it is both a predicate (musnad) and a subject of predication (musnad ilayhi) at once, with each of the two predications being complete;"},
    {"type": "matn",
     "ar": "بخلاف: «أعجبني ضرب زيد»؛ لأن أحد الإسنادين وهو إسناد المصدر غير تام.",
     "en": "unlike “Zayd’s being struck pleased me” (aʿjabanī ḍarbu Zaydin), because one of the two predications, namely the predication of the verbal noun (maṣdar), is not complete."},
    {"type": "matn",
     "ar": "(ولا) المفعول (الثالث من) مفاعيل (باب «أعلمت»[[١]])؛ إذ حكمه حكم المفعول الثاني من باب «علمت» في كونه مسندا.",
     "en": "(Nor—wa-lā) the (third—al-thālith) object (of—min) the objects of (the category of “aʿlamtu”—bāb aʿlamtu); for its rule is the rule of the second object of the category of “ʿalimtu” in its being a predicate."},
    {"type": "matn",
     "ar": "(والمفعول له) بلا لام[[٢]]؛ لأن النصب فيه مشعر بالعلية[[٣]]، فلو أسند إليه الفعل فات النصب والإشعار،",
     "en": "(And the object of purpose—wa-l-mafʿūl lahu) without lām; because the accusative (naṣb) in it signals causality (ʿilliyya), so were the verb predicated of it, the accusative and the signalling would be lost;"},
    {"type": "matn",
     "ar": "بخلاف ما إذا كان مع اللام، نحو: «ضرب للتأديب».",
     "en": "unlike when it comes with the lām, as in: “There was striking for the sake of discipline” (ḍuriba li-l-taʾdīb)."},
    {"type": "matn",
     "ar": "(والمفعول معه كذلك[[٤]]) أي: كل من المفعول له والمفعول معه كذلك، أي: كالمفعول الثاني والثالث من باب «علمت» و«أعلمت» في أنهما لا يقعان موقع الفاعل.",
     "en": "(And the object of accompaniment is likewise—wa-l-mafʿūl maʿahu ka-dhālika), that is: each of the object of purpose and the object of accompaniment is likewise, that is: like the second and third objects of the categories of “ʿalimtu” and “aʿlamtu,” in that the two of them do not occur in the position of the agent (fāʿil)."},
    {"type": "matn",
     "ar": "أما المفعول له، فلما عرفت.",
     "en": "As for the object of purpose, it is for the reason you have learned."},
    {"type": "matn",
     "ar": "وأما المفعول معه؛ فلأنه لا يجوز إقامته مقام الفاعل مع الواو التي أصلها العطف؛ إذ هي دليل الانفصال، والفاعل كالجزء من الفعل،",
     "en": "As for the object of accompaniment: because it is not permissible to set it in the place of the agent together with the wāw whose origin is conjunction (ʿaṭf), since [the wāw] is a sign of separation, whereas the agent is like a part of the verb;"},
    {"type": "matn",
     "ar": "ولا بدون الواو، فإنه لم يعرف حينئذ كونه مفعولا معه.",
     "en": "nor without the wāw, for then its being an object of accompaniment would not be known."},
    {"type": "matn",
     "ar": "(وإذا وجد المفعول به) في الكلام مع غيره من المفاعيل التي يجوز وقوعها موقع الفاعل (تعين) أي: المفعول به (له) أي: لوقوعه موقع الفاعل، لشدة شبهه بالفاعل[[٥]]",
     "en": "(And when the direct object is present—wa-idhā wujida al-mafʿūl bihi) in the utterance together with other objects that may occur in the position of the agent, (it is singled out—taʿayyana), that is: the direct object, (for it—lahu), that is: for occurring in the position of the agent, because of its strong resemblance to the agent…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "قلت: لو اكتفى بقوله: ولا الثالث لصح؛ لأنه لا ثالث إلا لباب «أعلمت».",
     "en": "I say: had he contented himself with saying “nor the third,” it would have been correct, because there is no third [object] except for the category of “aʿlamtu.”"},
    {"type": "pair",
     "ar": "قيل: لم يقع الثاني أيضا.",
     "en": "It has been said: the second [object of that category] does not occur [in the agent’s position] either."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قيل: مع اللام أيضا لا يقع.",
     "en": "It has been said: with the lām, too, it does not occur [in the agent’s position]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيل: النصب في الظرف أيضا مشعر بالظرفية، فلا بد من بيان فارق.",
     "en": "It has been said: the accusative in the adverb (ẓarf) also signals adverbiality (ẓarfiyya), so a distinguishing factor must be shown."},
    {"type": "pair",
     "ar": "ويمكن بيانه بأن ذات المفعول فيه يقتضي الظرفية، والنصب يدل على قصدها،",
     "en": "It can be shown thus: the very essence of the adverbial object (al-mafʿūl fīhi) requires adverbiality, and the accusative indicates that it is intended;"},
    {"type": "pair",
     "ar": "بخلاف المفعول له، فإن ذاته لا تقتضي العلية، وإنما يعلم عليته بالنصب كقصدها.",
     "en": "unlike the object of purpose, for its essence does not require causality; rather its causality is known only through the accusative, as is the intention of it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "نبه على أن الكلام من عطف الجملة الاسمية على الفعلية، وليس قوله: والمفعول له من قبيل عطف المفرد.",
     "en": "He indicated that the utterance is a case of conjoining a nominal sentence to a verbal one, and that his words “and the object of purpose” are not of the type of conjoining a single term (mufrad)."},
    {"type": "pair",
     "ar": "وإنما رجح هذا الاحتمال؛ لأن الأول يستدعي إعادة «لا» في المفعول له والمفعول معه،",
     "en": "He preferred this possibility only because the first would call for repeating “lā” with the object of purpose and the object of accompaniment;"},
    {"type": "pair",
     "ar": "وفي هذا الاحتمال تجديد أسلوب البيان، وجعل «كذلك» عمدة.",
     "en": "and in this possibility there is a renewal of the mode of exposition, and the making of “ka-dhālika” a principal element (ʿumda)."},
    {"type": "pair",
     "ar": "والأولى تفسير «كذلك» بالمفعول الثاني من باب «علمت» ليكون إشارة إلى واحد بعينه.",
     "en": "It is preferable to explain “ka-dhālika” by the second object of the category of “ʿalimtu,” so that it is a reference to one specific thing."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قيل: لبناء الفعل المجهول له، وكون إسناده إليه حقيقة، وإلى غيره مجازا.",
     "en": "It has been said: because the passive verb is constructed for it, and its predication to it is literal (ḥaqīqa), while to anything else it is figurative (majāz)."},
    {"type": "pair",
     "ar": "ولا يصار إلى غير الحقيقة مع إمكانها.",
     "en": "And one does not resort to the non-literal while the literal is possible."},
    {"type": "pair",
     "ar": "وفيه أن معنى قولهم: لا يصار إلى المجاز مع إمكان الحقيقة، أن الكلام إذا دار بين الحقيقة والمجاز، فالحمل على المعنى الحقيقي متعين؛",
     "en": "In this [there is a difficulty]: the meaning of their saying “one does not resort to the figurative while the literal is possible” is that when an utterance hovers between the literal and the figurative, construing it in the literal sense is required;"},
    # REVIEW: printed «لأن» here; the argument reads more naturally as «لا أن» ("not that"); translated as printed.
    {"type": "pair",
     "ar": "لأن المتكلم بالحقيقة متعين مع إمكان التكلم بالمجاز.",
     "en": "because the speaker is bound to the literal even while speaking figuratively is possible."},
    {"type": "pair",
     "ar": "فالأظهر أن يقال: إن الإسناد إلى ما سواه مجاز عقلي، ولا يمكن المجاز العقلي مع وجود ما هو له.",
     "en": "So the more evident [answer] is to say: predication to anything other than it is a rational metaphor (majāz ʿaqlī), and a rational metaphor is not possible when that to which [the act] properly belongs is present."},
]
