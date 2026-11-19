# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 556 (printed ٥٥٥)."""

PAGE_NUMBER = 556
PRINTED_PAGE = "٥٥٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لأن «ما»» at the foot of PDF p. 555 (mid-sentence).
    {"type": "matn",
     "ar": "الكافة أخرجتها عن العمل[[١]]، فلا يلزم أن يكون مدخولها صالحا للعمل.",
     "en": "…the restraining [mā] has removed them from governing, so what they enter upon need not be susceptible to their governing."},

    {"type": "section", "ar": "[إن وأن]",
     "en": "Inna and Anna"},

    {"type": "matn",
     "ar": "(فإن) المكسورة (لا تغير[[٢]] معنى الجملة[[٣]]) ولا تخرجها عن كونها جملة،",
     "en": "(Thus inna) with kasra (does not alter the meaning of the sentence) and does not remove it from being a sentence;"},
    {"type": "matn",
     "ar": "فإذا قلت: «إن زيدا قائم» أفدت به ما أفدت بقولك: «زيد قائم» مع زيادة التأكيد.",
     "en": "so when you say “inna Zaydan qāʾimun” (Zayd is indeed standing), you convey by it what you convey by saying “Zaydun qāʾimun” (Zayd is standing), with added corroboration."},
    {"type": "matn",
     "ar": "(وأن) المفتوحة (مع جملتها) أي: مع اسمها وخبرها، سماها جملة باعتبار ما كانت عليه قبل دخولها عليهما (في حكم المفرد[[٤]]).",
     "en": "(And anna) with fatḥa, (together with its sentence) — that is, with its noun and its predicate; he called it a sentence in view of what it was before anna entered upon them — (has the status of a single term (mufrad))."},
    {"type": "matn",
     "ar": "(ومن ثم) أي: ومن أجل الفرق المذكور (وجب الكسر في موضع الجمل) أي: في موضع يقتضي الجمل",
     "en": "(Hence), that is, because of the difference mentioned, (the kasra is required in the position of sentences), that is, in a position that requires sentences,"},
    {"type": "matn",
     "ar": "(و) وجب (الفتح في موضع المفرد) أي: في موضع يقتضي المفرد.",
     "en": "(and) (the fatḥa is required in the position of the single term), that is, in a position that requires a single term."},
    {"type": "matn",
     "ar": "(فكسرت «إن»[[٥]]):",
     "en": "(So “inna” takes kasra):"},
    {"type": "matn",
     "ar": "١-(ابتداء) أي: في ابتداء الكلام[[٦]]، لكونه موضع الجملة، نحو: «إن زيدا قائم».",
     "en": "1. (at the beginning), that is, at the beginning of speech, because it is the position of the sentence, as in “inna Zaydan qāʾimun”."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لأنها بسبب لحوقها وصيرورتها كالجزء منها ضعفت مشابهتها بالفعل من حيث البناء على الفتح.",
     "en": "Because, by its attaching to them and becoming like a part of them, their resemblance to the verb in respect of being fixed on the fatḥa was weakened."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الفاء بيان لتفصيل الأحوال المختصة بكل واحد منهما بعد بيان الأحكام المشتركة بينهما،",
     "en": "The fāʾ is an explanation, setting out in detail the states specific to each of the two after explaining the rulings common to them."},
    {"type": "pair",
     "ar": "ولم يبين معنى «إن» المكسورة والمفتوحة لشهرة كونهما للتأكيد،",
     "en": "He did not explain the meaning of “inna” with kasra and with fatḥa because their being for corroboration is well known:"},
    {"type": "pair",
     "ar": "فالمكسورة لتأكيد النسبة التامة، والمفتوحة لتأكيد النسبة الإضافية المسبوكة من الاسم والخبر.",
     "en": "the one with kasra is for corroborating the complete predicative relation, and the one with fatḥa is for corroborating the annexational relation cast [into a single term] from the noun and the predicate."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قال الشيخ الرضي: أخذ في تفصيل معاني الحروف الستة.",
     "en": "Al-Shaykh al-Raḍī said: he has begun setting out in detail the meanings of the six particles."},
    {"type": "pair",
     "ar": "ولا يخفى عليك أنه لم يبين لـ«أن وإن» معنى، فالأولى أخذ في تفصيل ما يتعلق بهذه الحروف.",
     "en": "It is not hidden from you that he has not explained a meaning for “anna and inna”; so it is better [to say]: he has begun setting out in detail what pertains to these particles."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "حيث لا يشتمل على إسناد تام يصح السكوت عليه.",
     "en": "In that it does not contain a complete predication on which it is proper to stop."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يحتمل أن يكون مفعول ما لم يسم فاعله، وأن يكون مفعولا به. وكذا في قوله: وفتحت أن.",
     "en": "It may be the object of a verb whose agent is not named [i.e. kusirat is passive], or it may be a direct object [i.e. kasarta, active]; likewise in his words “wa-futiḥat anna”."},
    {"type": "pair",
     "ar": "والمراد بأن هذه الكلمة مع قطع النظر عن الكسرة والفتحة.",
     "en": "What is meant by “an” is this word, setting aside the kasra and the fatḥa."},
    {"type": "pair",
     "ar": "قال العصام: نبه على «إن» كسرت مسندة إلى ضمير «أن» أو على أن مفعوله المحذوف «أن»،",
     "en": "Al-ʿIṣām said: he drew attention [by writing] “inna” to [the reading that] “kusirat” is predicated of a pronoun referring to “an”, or that its omitted object is “an”;"},
    {"type": "pair",
     "ar": "والمراد كسر هذه المادة، فلا يلزم تحصيل الحاصل.",
     "en": "and what is meant is putting the kasra on this material [word], so it does not entail producing what already exists (taḥṣīl al-ḥāṣil)."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    # REVIEW: «وسط كلامه المتكلم» printed thus (pronoun suffix with a following definite noun); transcribed as printed.
    {"type": "pair",
     "ar": "يحتمل ابتداء الكلام أول الكلام سواء كان وسط كلامه المتكلم، أو أوله، وعليه حمله الشارح الرضي.",
     "en": "“The beginning of speech” may mean the beginning of a sentence, whether it is in the middle of the speaker’s discourse or at its beginning; the commentator al-Raḍī took it in this sense."},
    {"type": "pair",
     "ar": "وحينئذ يتجه عليه أنه لا مقابلة بينه وبين كونه بعد القول، وبعد الموصول، بل هما تحت كون إن في ابتداء الكلام.",
     "en": "On this reading it is objected that there is no contrast between it and its coming after a verb of saying or after a relative, since both fall under inna’s being at the beginning of speech."},
    {"type": "pair",
     "ar": "وقد نبه عليه في شرح كلام المتن حيث قال: وكذا يكسر بعد القول.",
     "en": "He drew attention to this in commenting on the words of the matn, where he said: “and likewise it takes kasra after a verb of saying”."},
    {"type": "pair",
     "ar": "ويحتمل ابتداء كلام المتكلم المقابل لوسط كلامه، وحينئذ تقابل كونه بعد القول والموصول؛ لأنهما وسطا كلام المتكلم،",
     "en": "It may also mean the beginning of the speaker’s discourse, as opposed to its middle; on this reading it contrasts with its coming after a verb of saying or a relative, because these are in the middle of the speaker’s discourse."},
    {"type": "pair",
     "ar": "ولا يرد عليه إلا عدم استيفاء مواضع الكسر؛ لأن منها كونها في الأول جملة وقعت خبرا أو حالا أو جواب قسم.",
     "en": "The only objection to it is that it does not exhaust the positions of the kasra, since among them is its being at the start of a sentence that occurs as a predicate, a circumstantial clause, or the answer of an oath."},
]
