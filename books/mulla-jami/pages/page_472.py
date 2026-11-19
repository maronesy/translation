# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 472 (printed ٤٧١)."""

PAGE_NUMBER = 472
PRINTED_PAGE = "٤٧١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "(ولا يعمل) اسم التفضيل (في) اسم (مظهر)[[١]] الرفع بالفاعلية بقرينة الاستثناء[[٢]]،",
     "en": "(And) the elative (does not govern) the nominative as agent (fāʿil) (in an explicit) noun (ẓāhir), as the exception [that follows] indicates."},
    {"type": "matn",
     "ar": "وإنما خص المظهر[[٣]]؛ لأنه يعمل في المظهر بلا شرط؛ لأن العمل في المضمر ضعيف لا يظهر أثره في اللفظ، فلا يحتاج إلى قوة العامل،",
     "en": "He specified the explicit noun only because it governs [a pronoun] without condition, since government in a pronoun is weak, its effect not appearing in the wording, so it does not need a strong governor (ʿāmil)."},
    {"type": "matn",
     "ar": "وإنما خص بالفاعل؛ لأنه لا ينصب المفعول به سواء كان مظهرا أو مضمرا،",
     "en": "He specified the agent only because it does not put the direct object (mafʿūl bihi) in the accusative, whether explicit or a pronoun;"},
    {"type": "matn",
     "ar": "بل إن وجد بعده ما يوهم ذلك فـ«أفعل» دال على الفعل الناصب له، كقوله تعالى: ﴿هو أعلم من يضل عن سبيله﴾[[٤]] أي: أعلم من كل أحد يعلم من يضل،",
     "en": "rather, if something occurs after it that suggests this, then “afʿal” indicates the verb that puts it in the accusative, as in His words, the Exalted: “He is most knowing of who strays from His path”, that is, more knowing than anyone, [He] knows who strays."},
    {"type": "matn",
     "ar": "وأما الظرف والحال والتمييز، فيعمل فيها أيضا بلا شرط؛ لأن[[٥]] الظرف والحال تكفيهما رائحة من الفعل نحو: «زيد أحسن منك اليوم راكبا»،",
     "en": "As for the adverbial of time or place (ẓarf), the circumstantial (ḥāl) and the specifier (tamyīz), it also governs them without condition, because a mere scent of the verb suffices for the ẓarf and the ḥāl, as in “Zayd is more handsome than you today, riding”;"},
    {"type": "matn",
     "ar": "والتمييز ينصبه ما يخلو عن معنى الفعل أيضا نحو: «رطل زيتا»،",
     "en": "and the tamyīz is put in the accusative even by what is devoid of the meaning of the verb, as in “a raṭl of oil”."},
    {"type": "matn",
     "ar": "وإنما لم يعمل الرفع بالفاعلية؛ لأن هذا العمل بالأصالة إنما هو عمل الفعل، وهو لم يعمل[[٦]] عمل الفعل؛",
     "en": "It does not govern the nominative as agent only because this government belongs originally to the verb, and it does not perform the government of the verb,"},
    {"type": "matn",
     "ar": "لأنه ليس له فعل بمعناه في الزيادة ليعمل عمله، ولأنه لما كان فيما هو",
     "en": "since it has no verb with its meaning of excess whose government it could perform; and because, since it was, in what is…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: أن الحكم بنفي عمله في المظهر مطلقا لا يصح؛",
     "en": "He means: the judgement denying its government in an explicit noun absolutely is not sound,"},
    {"type": "pair",
     "ar": "لأنه يعمل في الظرف والحال والتمييز والمفعول به بواسطة حرف الجر، نحو: زيد أضرب لعمرو،",
     "en": "because it governs the ẓarf, the ḥāl, the tamyīz, and the object by means of a preposition, as in “Zayd is a harder striker of ʿAmr”;"},
    {"type": "pair",
     "ar": "فلا بد من التقييد ليصلح قرينة على التقييد بالفاعل والمفعول به بلا واسطة.",
     "en": "so a restriction is necessary, to serve as an indication of the restriction to the agent and the object without intermediary."},
    {"type": "pair",
     "ar": "فقيدنا بالفاعل، فاندفع ما قيل: إنه يصلح حمله على الإطلاق والاستثناء من مطلق العمل يكون متحققا في ضمن الرفع بالفاعلية.",
     "en": "So we restricted it to the agent, and thereby what has been said is repelled: that it can be taken as absolute, the exception from government in general being realized within the nominative as agent."},
    {"type": "pair",
     "ar": "والمعنى لا يعمل في المظهر مطلقا إلا في صورة الاستثناء، فإنه يعمل فيها بالرفع.",
     "en": "The meaning [on that view] is: it does not govern an explicit noun at all except in the case of the exception, for there it governs it with the nominative."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وجه كون الاستثناء قرينة أن العمل في المستثنى بالرفع على الفاعلية،",
     "en": "The reason the exception is an indication is that the government in the excepted [noun] is the nominative as agent."},
    {"type": "pair",
     "ar": "وفيه بحث لأنه يصح الاستثناء مع بقاء العمل على عمومه يعني: لا يعمل أصلا في مضمر إلا في مظهر،",
     "en": "This is open to discussion, because the exception is sound with government remaining general, meaning: it does not govern at all in a pronoun except in an explicit noun;"},
    {"type": "pair",
     "ar": "كذا غايته أن العمل في هذا المظهر لا يتصور إلا بالفاعلية.",
     "en": "so too; the most that follows is that government in this explicit noun is conceivable only as agent."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "في المغني في باب الظرف: ومن المشكل قوله: فخير نحن عند الناس منكم",
     "en": "In al-Mughnī, in the chapter on the ẓarf: “Among the problematic [cases] is his saying: ‘So better are we, in people’s eyes, than you’;"},
    {"type": "pair",
     "ar": "لأن قوله: «نحن» إن قدر فاعلا لزم إعمال الوصف غير معتمد، ولم يثبت.",
     "en": "for if his word ‘naḥnu’ is taken as agent, it entails the government of an adjective that does not rest [on a preceding element], and that is not established;"},
    {"type": "pair",
     "ar": "وعمل أفعل في الظاهر في غير مسألة الكحل وهو ضعيف.",
     "en": "and the government of afʿal in an explicit noun outside the kuḥl question, which is weak."},
    {"type": "pair",
     "ar": "وإن قدر مبتدأ لزم الفصل به وهو أجنبي من أفعل ومن.",
     "en": "If it is taken as a mubtadaʾ, it entails separating afʿal and min by it, while it is foreign to them."},
    {"type": "pair",
     "ar": "وخرجه أبو علي وتبعه ابن خروف على أن الوصف خبر لنحن محذوفة، وقدر نحن المذكور تأكيدا للضمير في أفعل، انتهى.",
     "en": "Abū ʿAlī, followed by Ibn Kharūf, explained it as the adjective being the predicate of an elided ‘naḥnu’, and took the ‘naḥnu’ that is mentioned as a corroboration of the pronoun in afʿal.” End of quotation."},
    # REVIEW: printed «على نص عليه» (one would expect «على ما نص عليه» or «كما نص عليه»); also «وأن المراد بالضمير المستتر» seems to lack a predicate. Transcribed as printed; translated by sense.
    {"type": "pair",
     "ar": "وعلم من كلامه أن المراد من المظهر ههنا ما يعم الضمير البارز، وأن المراد بالضمير المستتر على نص عليه في الرضي،",
     "en": "It is known from his words that by “explicit noun” here is meant what includes the overt pronoun, and that by “pronoun” is meant the concealed pronoun, as stated explicitly in al-Raḍī;"},
    # REVIEW: printed «أنه لفظ لا أثر» — the sense is obscure (perhaps «أنه لا لفظ له لا أثر»); transcribed as printed, translated literally.
    {"type": "pair",
     "ar": "وأن معنى قوله: لا يظهر أثره في اللفظ أنه لفظ لا أثر.",
     "en": "and that the meaning of his words “its effect does not appear in the wording” is that it is wording, not effect."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة الأنعام: ١١٧.",
     "en": "(Qurʾān, Sūrat al-Anʿām 6:117)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "يدفع النقض بأن هذا الاستدلال يقتضي ألا يعمل في المظهر مطلقا.",
     "en": "He repels the objection that this reasoning requires that it not govern an explicit noun at all."},
    {"type": "pair",
     "ar": "وحاصل الدفع: عمل الرفع بالأصالة للفعل بخلاف النصب، فإنه يعم الفعل والحرف، فيعمل النصب ما هو مشابهه في الجملة وإن لم يكن.",
     "en": "The gist of the reply: governing the nominative belongs originally to the verb, unlike the accusative, which is common to verb and particle; so the accusative is governed by what resembles it in some measure, even if it is not [a verb]."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: اسم التفضيل لم يعمل عمل الفعل أصلا؛ لأنه ليس له فعل بمعناه، فلذا لم يعمل الرفع، فلا مصادرة.",
     "en": "That is, the elative does not perform the government of the verb at all, because it has no verb with its meaning; for that reason it does not govern the nominative, so there is no begging of the question (muṣādara)."},
]
