# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 44 (printed ٤٣)."""

PAGE_NUMBER = 44
PRINTED_PAGE = "٤٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "القسم حرفا؛ لأن الحرف في اللغة: الطرف، وهو في طرف، أي: في جانب مقابل للاسم والفعل حيث يقعان عمدة في الكلام[[١]]، وهو لا يقع[[٢]] عمدة فيه، كما ستعرف.",
     "en": "…this category “ḥarf,” because “ḥarf” in the language means “the edge/extremity” (al-ṭaraf); and it lies at an extremity — that is, on a side opposite to the noun and the verb — since the two occur as principal elements (ʿumda) in speech, whereas it does not occur as a principal element in it, as you will come to know."},
    {"type": "matn",
     "ar": "(و) القسم (الأول) وهو ما يدل على معنى في نفسها: (إما) من صفتها: (أن يقترن) ذلك المعنى[[٣]] المدلول عليه بنفسها في الفهم عنها (بأحد الأزمنة الثلاثة)[[٤]] أعني: الماضي، والحال[[٥]]، والاستقبال[[٦]]،",
     "en": "(And) the (first) category — which is that which signifies a meaning in itself — is: (either) — among its attributes — (that) that meaning, signified by it in itself in what is understood from it, (be conjoined with one of the three times), namely: the past, the present, and the future;"},
    {"type": "matn",
     "ar": "أي: حين يفهم ذلك المعنى[[٧]] عنها يفهم أحد الأزمنة الثلاثة أيضا مقارنا له[[٨]].",
     "en": "that is: when that meaning is understood from it, one of the three times is also understood as concurrent with it."},
    {"type": "matn",
     "ar": "(أو) من صفتها: أن (لا) يقترن ذلك المعنى المدلول عليه بنفسها في الفهم عنها مع أحد الأزمنة الثلاثة.",
     "en": "(Or) — among its attributes — (that) that meaning, signified by it in itself in what is understood from it, (be not) conjoined with one of the three times."},
    {"type": "matn",
     "ar": "القسم (الثاني): وهو ما يدل على معنى في نفسها غير مقترن بأحد الأزمنة الثلاثة (الاسم). وهو مأخوذ من السمو، وهو العلو، لاستعلائه[[٩]] على أخويه[[١٠]]، حيث يتركب منه وحده الكلام دون أخويه.",
     "en": "The (second) category — which is that which signifies a meaning in itself, not conjoined with one of the three times — is (the noun, al-ism). It is derived from al-sumuww, meaning elevation, on account of its exalting itself above its two brothers, since speech may be composed of it alone, apart from its two brothers."},
    {"type": "matn",
     "ar": "وقيل[[١١]]: من الوسم، وهو العلامة؛ لأنه علامة على مسماه.",
     "en": "And it is said: [it is derived] from al-wasm, meaning the mark, because it is a mark for the thing it names (musammā)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لأن مفهومه في طرف مقابل لمفهومهما، وهو كونه ما لا يدل على معنى في نفسه.",
     "en": "Because its concept is at an edge opposite to the concept of the two of them — namely, its being that which does not signify a meaning in itself."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: لا يقع عمدة مستقلة، وإن وقع جزءا منها في بعض المواد.",
     "en": "That is: it does not occur as an independent principal element, even if it occurs as a part of one in some instances (mawādd)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أرجع الضمير المستتر في «أن يقترن» إلى «المعنى»؛ لأنه المقترن حقيقة بأحد الأزمنة، لكن وصف الكلمة بالاقتران حينئذ من قبيل الوصف بحال المتعلق.",
     "en": "He referred the concealed pronoun in “an yaqtarin” back to “the meaning,” because it is what is in reality conjoined with one of the times; yet describing the word as “conjoined” in that case is of the type of describing [a thing] by the state of what pertains to it (ḥāl al-mutaʿallaq)."},
    {"type": "pair",
     "ar": "ويجوز إرجاعه إلى الكلمة بأن يقرأ «تقترن» بالتاء، ويراد بالاقتران اقتران الدال بالمدلول، لكن التعبير من الحال الواقعة بين الدال والمدلول بالاقتران غير شائع.",
     "en": "It is permissible to refer it back to “the word,” by reading “taqtarin” [with tāʾ], intending by “conjunction” the conjunction of the signifier (dāll) with the signified (madlūl); but expressing the relation obtaining between signifier and signified by “conjunction” is uncommon."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الإضافة للعهد الذهني، والثلاثة صفة الأزمنة. وأورد عليه بأن الثلاثة مذكر والأزمنة مؤنث، فلا مطابقة بينهما، وأن الأزمنة جمع والثلاثة مفرد.",
     "en": "The genitive construction is for notional determination (al-ʿahd al-dhihnī), and “three” is an attribute of “the times.” An objection was raised: that “three” is masculine while “the times” (al-azmina) is feminine, so there is no agreement between them; and that “the times” is a plural while “three” is singular."},
    {"type": "pair",
     "ar": "وأجيب عن ذلك: بأن اسم العدد إذا وقع صفة الجمع أو خبرا أو مضافا إليه لا يقع صفة لمفرده أو خبرا أو مضافا إليه، نحو: «والأسباب المانعة تسعة»، و«سبع ليال وثمانية أيام». والنكتة فيه أنه إذا وقع صفة لجمع إن اعتبر أقل الجمع يلزم أن يكون الأزمنة تسعة، وإن اعتبر ما فوقه يلزم أن يزاد.",
     "en": "It was answered: that a numeral noun, when it falls as an attribute of the plural, or a predicate, or a governed genitive (muḍāf ilayhi), does not [also] fall as an attribute of its singular, or a predicate, or a governed genitive — as in “and the preventing causes are nine” (wa-l-asbāb al-māniʿa tisʿa), and “seven nights and eight days” (sabʿa layālin wa-thamāniyata ayyām). The subtle point (nukta) in it is that, when it falls as an attribute of a plural, if the minimal plural be reckoned, the times would have to be nine; and if more than that be reckoned, [the count] would have to be increased."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إشارة إلى أن اللام في المتن للعهد الخارجي العلمي. فلا يرد حين إذا وقع هذا اللفظ في الحدود إيراد الألفاظ المبهمة المجملة في التعريفات ولو كانت ضمنية.",
     "en": "[It is] a pointer that the lām (definite article) in the matn is for the well-known external determination (al-ʿahd al-khārijī al-ʿilmī). So there does not arise — at the time when this term occurs among the definitions (ḥudūd) — the objection of introducing vague, undefined terms into definitions, even if [they be] implicit."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الحال: ما أنت فيه في زمان التكلم بالدال على الزمان، والماضي: ما تقدم عليه، والاستقبال: ما تأخر عنه.",
     "en": "The present (al-ḥāl): that which you are in, at the time of speaking, by [reference to] that which indicates time; the past (al-māḍī): that which precedes it; and the future (al-istiqbāl): that which comes after it."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "تفسير لقوله: «أن يقترن»، وبيان لحاصل المعنى.",
     "en": "An explanation of his statement “that it be conjoined,” and a clarification of the upshot of the meaning."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "حال من المعنى، أي: حال كونه مقارنا لأحد الأزمنة. وفيه رمز إلى أن الاقتران بمعنى المقارنة، ثم إنه مقارنة المظروف بالظرف كما لا يخفى.",
     "en": "[It is] a circumstantial qualifier (ḥāl) from “the meaning” — that is, in the state of its being concurrent with one of the times. In it is an indication that “conjunction” (iqtirān) means “concurrence” (muqārana); moreover, that it is the concurrence of the contained (maẓrūf) with the container (ẓarf) is, as [is evident], not hidden."},

    # ---------------- Footnote 9 ----------------
    {"type": "note", "num": "٩"},
    {"type": "pair",
     "ar": "لأنه يرفع المسمى.",
     "en": "Because it raises up the thing named (musammā)."},

    # ---------------- Footnote 10 ----------------
    {"type": "note", "num": "١٠"},
    {"type": "pair",
     "ar": "أي: مثليه، أعني: الفعل والحرف، ففيه مجاز.",
     "en": "That is: its two likes — namely, the verb and the particle; so there is in it a figurative usage (majāz)."},

    # ---------------- Footnote 11 ----------------
    {"type": "note", "num": "١١"},
    {"type": "pair",
     "ar": "وهو الكوفيين. ووجه التمريض كون مذهبهم مرجوحا.",
     "en": "That is, [the view of] the Kūfans. The reason for the weakening [expression “it is said,” qīla] is that their position is the outweighed one (marjūḥ)."},
]
