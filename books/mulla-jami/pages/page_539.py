# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 539 (printed ٥٣٨)."""

PAGE_NUMBER = 539
PRINTED_PAGE = "٥٣٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «أي: كلمة دلت على معنى حاصل في غيرها» at the foot of PDF p. 538 (mid-sentence).
    {"type": "matn",
     "ar": "متعقل بالنسبة إليه[[١]]، أي: لا يكون مستقلا بالمفهومية بحيث لا يصلح لأن يحكم عليه أو به،",
     "en": "…and conceived in relation to it; that is, it is not independent in being understood, such that it is not fit to be the subject or the predicate of a judgement;"},
    {"type": "matn",
     "ar": "بل لا بد له في ذلك من انضمام أمر آخر إليه.",
     "en": "rather, for that it must have something else joined to it."},
    {"type": "matn",
     "ar": "(ومن ثمة) أي: لأجل أنه يدل على معنى في غيره (احتاج في جزئيته) للكلام[[٢]] ركنا كان أو غيره",
     "en": "(Hence), that is, because it signifies a meaning in something other than itself, (it needs, for its being a part) of speech, whether a pillar [of it] or otherwise,"},
    {"type": "matn",
     "ar": "(إلى اسم) يتعقل معناه[[٣]] بالنسبة إليه، نحو: «من البصرة»، (أو فعل[[٤]]) كذلك نحو: «قد ضرب».",
     "en": "(a noun) in relation to which its meaning is conceived, as in “min al-Baṣrati” (from Baṣra), (or a verb) likewise, as in “qad ḍaraba” (he has struck)."},

    {"type": "section", "ar": "[حروف الجر]",
     "en": "The Prepositions (Ḥurūf al-Jarr)"},

    {"type": "matn",
     "ar": "(حروف الجر: ما وضع للإفضاء بفعل) أي: إيصاله.",
     "en": "(The prepositions (ḥurūf al-jarr) are what is coined for conveying a verb), that is, for making it reach."},
    {"type": "matn",
     "ar": "فإن معنى الإفضاء الوصول، ولما عدي بالباء صار معناه الإيصال.",
     "en": "For the meaning of ifḍāʾ is “reaching”, and when it is made transitive with the bāʾ its meaning becomes “making reach”."},
    {"type": "matn",
     "ar": "(أو معناه) أي: معنى الفعل، وهو كل شيء استنبط منه معنى الفعل؛ كاسمي الفاعل، والمفعول، والصفة المشبهة، والمصدر، والظرف، والجار والمجرور، وغير ذلك.",
     "en": "(Or its meaning), that is, the meaning of the verb, which is anything from which the meaning of the verb is drawn, such as the active and passive participles, the assimilated adjective (al-ṣifa al-mushabbaha), the verbal noun, the adverbial, the preposition with its object, and so on."},
    {"type": "matn",
     "ar": "(إلى ما يليه) سواء كان اسما صريحا، مثل: «مررت بزيد» و«أنا مار بزيد»",
     "en": "(to what follows it), whether it is an explicit noun, as in “I passed by Zayd” and “I am passing by Zayd”,"},
    {"type": "matn",
     "ar": "أو كان في تأويل الاسم، كقوله تعالى: ﴿ضاقت عليهم الأرض بما رحبت﴾[[٥]] أي: برحبها.",
     "en": "or is construed as a noun, as in His words, the Exalted: “the earth, for all its spaciousness (bi-mā raḥubat), closed in on them”, that is, bi-ruḥbihā (for all its spaciousness)."},
    {"type": "matn",
     "ar": "وسميت هذه الحروف[[٦]] «حروف الإضافة» أيضا؛ لأنها تضيف الفعل أو معناه إلى ما يليه،",
     "en": "These particles are also called “particles of annexation” (ḥurūf al-iḍāfa), because they annex the verb or its meaning to what follows it;"},
    {"type": "matn",
     "ar": "و«حروف الجر»: لأنها تجر معاني الأفعال إلى ما يليه، أو لأن أثرها[[٧]]",
     "en": "and “particles of drawing” (ḥurūf al-jarr), because they draw the meanings of verbs to what follows, or because their effect…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "صفة كاشفة لـ«حاصل في غيرها»، فإن حصول المعنى في غير الكلمة يحتمل أن يكون باعتبار اتصاف الغيرية،",
     "en": "An explicative qualifier of “realized in something other than it”; for the meaning’s being realized in something other than the word could be in respect of [that other’s] being qualified by it,"},
    {"type": "pair",
     "ar": "وأن يكون باعتبار دلالته عليه، وأن يكون باعتبار تعقله بالنسبة إليه.",
     "en": "or in respect of its signifying it, or in respect of its being conceived in relation to it."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بخلاف الاسم والفعل، فإنه لا يحتاج أحدهما إلى الآخر في الجزئية، بل في تأتي الكلام.",
     "en": "Unlike the noun and the verb, for neither of them needs the other in being a part, but only in the realization of speech."},
    {"type": "pair",
     "ar": "ومن هذا ظهر وجه التخصيص بالكلام، واندفع ما قيل: الأولى أن يقال في جزئيته لما يقاربه شيء كلاما كان أو مركبا ناقصا.",
     "en": "From this the reason for restricting [it] to speech becomes clear, and what was said is repelled: that it would be better to say “in its being a part of whatever something joins it in, whether speech or an incomplete compound”."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيد الاسم والفعل بهذا القيد بقرينة المقام، لئلا يرد الموصولات، فإنها محتاجة في الجزئية إلى اسم أو فعل،",
     "en": "He restricted the noun and the verb by this qualification, as the context indicates, so that the relative nouns not be raised as an objection; for they need, in being a part, a noun or a verb;"},
    {"type": "pair",
     "ar": "لكن ليس ذلك مما يتعقل معناها بالنسبة إليه، لكون معانيها مستقلة بالمفهومية.",
     "en": "but that is not something in relation to which their meaning is conceived, since their meanings are independent in being understood."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "«أو» لمنع الخلو.",
     "en": "“Aw” (or) is for excluding the absence of both (manʿ al-khulūw)."},
    {"type": "pair",
     "ar": "قال الرضي: الحرف قد يحتاج إلى المفرد كما ذكرنا، وقد يحتاج إلى الجملة كحرف النفي والاستفهام والشرط،",
     "en": "Al-Raḍī said: the particle sometimes needs a single term, as we have mentioned, and sometimes needs a sentence, like the particles of negation, interrogation and condition;"},
    # REVIEW: printed «و«كأن» «قد» خرجت و«لما»» — no «و» between «كأن» and «قد», and «خرجت» stands outside the guillemets; read as the elliptical «كأن قد» and «خرجت ولما». Transcribed as printed.
    {"type": "pair",
     "ar": "وقد يحذف المحتاج إليه في «نعم» و«لا» و«كأن» «قد» خرجت و«لما».",
     "en": "and what is needed is sometimes omitted, as in “naʿam” (yes), “lā” (no), “ka-an qad” (as though already), and “kharajtu wa-lammā” (I went out, and not yet)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة التوبة: ١١٨.",
     "en": "Qurʾān, Sūrat al-Tawba 9:118."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قدمها على بيان وجه التسمية بحرف الجر، وإن كان الظاهر يقتضي تأخيرها؛",
     "en": "He put it before explaining the reason for the name “particle of jarr”, even though the obvious order requires putting it later,"},
    {"type": "pair",
     "ar": "لأن العلم بالاسم أهم بالنسبة إلى المتعلم في العلم بوجه التسمية.",
     "en": "because knowing the name matters more to the learner than knowing the reason for the naming."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الجر اسم للإعراب المخصوص اصطلاحا كما في قولهم: حروف النصب وحروف الجزم.",
     "en": "Jarr is, technically, the name of the particular inflection [the genitive], as in their expressions “particles of the accusative” and “particles of the jussive”."},
]
