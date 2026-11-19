# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 526 (printed ٥٢٥)."""

PAGE_NUMBER = 526
PRINTED_PAGE = "٥٢٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… (لابن كيسان) بأن يكون هذا الخلاف» at the foot of PDF p. 525 (mid-sentence).
    {"type": "matn",
     "ar": "واقعا ظاهرا من جانبه لا من جانب الجمهور -كما يقتضيه باب المفاعلة[[١]]- لتقدمهم، فكأنه لا مخالفة منهم[[٢]]،",
     "en": "…arising and apparent from his side, not from the side of the majority, as the pattern mufāʿala requires, because they preceded [him]; so it is as though there were no opposition from them."},
    {"type": "matn",
     "ar": "وذلك الخلاف منه (في غير «ما دام»)؛ لأن أداة النفي لما دخلت على الفعل الذي معناه النفي أفادت الثبوت، فصار بمنزلة «كان»، فلا يلزم تقديم ما في حيز النفي بحسب المعنى.",
     "en": "That disagreement of his is (in what is other than “mā dāma”), because when the particle of negation enters upon a verb whose meaning is negation, it conveys affirmation, so it becomes equivalent to “kāna”; hence there results no placing first of what lies within the scope of negation, in terms of meaning."},
    {"type": "matn",
     "ar": "٣-(وقسم مختلف فيه) ظهر فيه الخلاف من الجمهور من بعضهم مع بعض،",
     "en": "3. (And a class that is disputed [mukhtalaf fīhi]), in which disagreement has appeared within the majority, some of them against others;"},
    {"type": "matn",
     "ar": "فإن «الافتعال» ههنا بمعنى «التفاعل» المقتضي لمشاركة أمرين في أصل الفعل صريحا.",
     "en": "for the pattern iftiʿāl here is in the sense of tafāʿul, which requires the explicit participation of two parties in the root action."},
    {"type": "matn",
     "ar": "(وهو) أي: القسم المختلف فيه كلمة («ليس»)",
     "en": "(And it), that is, the disputed class, is the word (“laysa”)."},
    {"type": "matn",
     "ar": "فالمبرد والكوفيون وابن السراج والجرجاني على أنه لا يجوز مراعاة للنفي؛ إذ يمتنع تقديم معمول النفي عليه،",
     "en": "Al-Mubarrad, the Kūfans, Ibn al-Sarrāj and al-Jurjānī hold that it is not permissible, out of regard for the negation, since what is governed by a negation cannot be placed before it;"},
    {"type": "matn",
     "ar": "والبصريون وسيبويه والسيرافي والفارسي على أنه يجوز بناء على أنه فعل، وجواز تقديم معمول الفعل عليه،",
     "en": "while the Baṣrans, Sībawayh, al-Sīrāfī and al-Fārisī hold that it is permissible, on the basis that it is a verb and that what a verb governs may be placed before it."},
    {"type": "matn",
     "ar": "وبين الطائفتين في حكم هذا القسم معارضة ومجادلة،",
     "en": "Between the two parties there is opposition and dispute over the ruling on this class."},
    {"type": "matn",
     "ar": "وبهذا اندفع ما قيل: كان[[٣]] من الواجب على المصنف أن يجعل ما في أوله «ما» النافية من القسم المختلف فيه؛ لوقوع الخلاف فيها من ابن كيسان.",
     "en": "By this is repelled what has been said: that the author ought to have placed what begins with negative “mā” in the disputed class, because disagreement about it occurred from Ibn Kaysān."},

    {"type": "rule"},

    # ---------------- Footnote continued from PDF p. 525 (note ٨ there) ----------------
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "يخصه بل الكوفيون أيضا خالفوا في ذلك ما عدا الفراء وهم.",
     "en": "…peculiar to him, but the Kūfans too, except al-Farrāʾ, disagreed on this, is a mistake."},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "من كون أحد الجانبين فاعلا صريحا، والآخر مفعولا صريحا.",
     "en": "Namely that one of the two sides is explicitly the agent and the other explicitly the object."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "ولا يتحقق التخالف المقتضي للمشاركة في أصل الفعل صريحا، فلا يندرج القسم الثاني في القسم الثالث.",
     "en": "So the mutual opposition that requires explicit participation in the root action is not realized, and the second class is not included in the third class."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وجه الدفع: أن المراد بالخلاف عدم اجتماع المخالفين، وتأخر المخالف.",
     "en": "The ground of the repelling is that what is meant by khilāf (opposition) is that the opposing parties are not contemporaneous, and that the opponent comes later;"},
    {"type": "pair",
     "ar": "والمراد بالاختلاف كون المخالفين معاصرين منازعين دل عليه قوله: بأن يكون هذا الخلاف واقعا ظاهرا من جانبه لا من جانب الجمهور، كما يقتضيه باب المفاعلة لتقدمهم.",
     "en": "while what is meant by ikhtilāf (disagreement) is that the opposing parties are contemporaries contending with each other. This is indicated by his words: “in that this disagreement is arising and apparent from his side, not from the side of the majority, as the pattern mufāʿala requires, because they preceded [him]”."},
    {"type": "pair",
     "ar": "وحاصل الكلام: ضعف جانب المخالف في الخلاف، فإنه كمخالفة الإجماع وعدم ضعف جانب في الاختلاف؛ لأنه ليس فيه خلاف ما تقرر.",
     "en": "The upshot of the discussion is the weakness of the opponent’s side in khilāf, for it is like opposing consensus, and the absence of weakness of either side in ikhtilāf, because it involves no opposition to what has been settled."},
    {"type": "pair",
     "ar": "ويمكن وجهان آخران ليميز \"ليس\" عن الأفعال المنفية:",
     "en": "Two further ways are possible of distinguishing “laysa” from the negated verbs:"},
    {"type": "pair",
     "ar": "أحدهما: أن المراد بالمختلف فيه ما اختلف فيه اللغات لا ما اختلف فيه النحاة،",
     "en": "First: that what is meant by “disputed” is that on which the dialects differ, not that on which the grammarians differ;"},
    {"type": "pair",
     "ar": "فجعل المصنف اختلاف النحاة في \"ليس\" من قبيل اختلاف اللغات، ودفع الاختلاف بينهم بخلاف مخالفة ابن كيسان، فإنه للخطأ في اللغة.",
     "en": "so the author treated the grammarians’ disagreement over “laysa” as a matter of dialectal difference, and removed the disagreement among them, unlike Ibn Kaysān’s opposition, which is due to an error about the language."},
    {"type": "pair",
     "ar": "وثانيهما: أنه لم يتعين المخالفون عند المصنف في \"ليس\" بخلاف الأفعال المنفية.",
     "en": "Second: that the opponents concerning “laysa” were not identified for the author, unlike [those concerning] the negated verbs."},
    {"type": "pair",
     "ar": "قال عبد الحكيم: حاصله الفرق بين الاختلاف والخلاف:",
     "en": "ʿAbd al-Ḥakīm said: its upshot is the difference between ikhtilāf and khilāf:"},
    {"type": "pair",
     "ar": "فإن الأولى لمشاركة أمرين في أصل الفعل صريحا، فيقتضي وقوع الفعل من الجانبين معا، والثاني يقتضي وقوع الفعل من أحد الجانبين صريحا.",
     "en": "the first is for the explicit participation of two parties in the root action, so it requires the action to occur from both sides together; the second requires the action to occur explicitly from one of the two sides."},
]
