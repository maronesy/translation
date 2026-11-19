# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 446 (printed ٤٤٥)."""

PAGE_NUMBER = 446
PRINTED_PAGE = "٤٤٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «مما هو اسم» at the foot of PDF p. 445 (mid-sentence).
    {"type": "matn",
     "ar": "جمع (ليس بجمع على الأصح) بل الأول اسم جنس، والثاني اسم جمع كالجماعة،",
     "en": "…collective noun, (is not a plural, according to the soundest view); rather, the first is a generic noun and the second a collective noun, like “jamāʿa” (group)."},
    {"type": "matn",
     "ar": "وقد علمت أنهما خارجان عن حد المجموع، والفرق بينهما أن اسم الجنس يقع على الواحد والاثنين وضعا، بخلاف اسم الجمع.",
     "en": "You have learned that both fall outside the definition of the plural. The difference between them is that the generic noun applies to one and to two by coinage, unlike the collective noun."},
    {"type": "matn",
     "ar": "فإن قيل: الكلم لا يقع على الكلمة والكلمتين، وهو جنس؟",
     "en": "If it is said: “kalim” does not apply to one word or to two words, yet it is a generic noun?"},
    {"type": "matn",
     "ar": "قيل: ذلك[[١]] بحسب الاستعمال لا بالوضع على أنه لا ضير[[٢]] في التزام كون الكلم اسم جمع أيضا.",
     "en": "It is answered: that is by usage, not by coinage; besides, there is no harm in holding that “kalim” is also a collective noun."},
    {"type": "matn",
     "ar": "وإنما قال: «على الأصح» وهو قول سيبويه؛ لأن الأخفش قال: جميع أسماء الجموع التي لها آحاد من تركيبها كـ«جامل وباقر وركب» جمع.",
     "en": "He said “according to the soundest view”, which is the view of Sībawayh, only because al-Akhfash said: all collective nouns that have units from their own root, like “jāmil” (a herd of camels), “bāqir” (a herd of cattle) and “rakb”, are plurals."},
    {"type": "matn",
     "ar": "وقال الفراء: وكذا أسماء الأجناس كـ«تمر وتمرة ونخل ونخلة»، وأما اسم جنس أو جمع لا واحد له من لفظه نحو: «إبل وغنم» فليس بجمع بالاتفاق.",
     "en": "Al-Farrāʾ said: and likewise the generic nouns, like “tamr” and “tamra”, “nakhl” and “nakhla”. As for a generic or collective noun that has no unit from its own wording, like “ibil” (camels) and “ghanam” (sheep), it is not a plural by agreement."},
    {"type": "matn",
     "ar": "(ونحو: «فلك») مما يكون الجمع والواحد فيه متحدين بالصورة (جمع) لصدق الحد عليه؛",
     "en": "(And the like of “fulk”) (ship, ships), among those in which the plural and the singular are identical in form, (is a plural), because the definition holds true of it;"},
    {"type": "matn",
     "ar": "فإن التغير المأخوذ فيه أعم من أن يكون بحسب الحقيقة أو بحسب التقدير، فضمة «فلك» إذا كان مفردا ضمة «قفل»، وإذا كان جمعا ضمة «أسد».",
     "en": "for the change taken into it is more general than being real or supposed: the ḍamma of “fulk”, when it is singular, is the ḍamma of “qufl” (lock), and when it is plural, the ḍamma of “usd” (lions)."},
    {"type": "matn",
     "ar": "(وهو) أي: المجموع نوعان: (صحيح ومكسر).",
     "en": "(And it), that is, the plural, is of two kinds: (sound and broken)."},
    {"type": "matn",
     "ar": "(فالصحيح) أي: الجمع الصحيح تارة يكون (لمذكر[[٣]] و) تارة يكون (لمؤنث)",
     "en": "(So the sound), that is, the sound plural, is sometimes (for a masculine, and) sometimes (for a feminine)."},
    {"type": "matn",
     "ar": "فالجمع الصحيح (المذكر: ما لحق آخره) أي: آخر مفرده (واو مضموم ما قبلها[[٤]]) في حالة الرفع (أو ياء مكسور ما قبلها) في حالتي النصب والجر",
     "en": "So the sound plural (of the masculine is that at whose end is attached), that is, at the end of its singular, (a wāw preceded by a ḍamma) in the nominative state, (or a yāʾ preceded by a kasra) in the accusative and genitive states,"},
    {"type": "matn",
     "ar": "(ونون) عوضا عن الحركة، أو التنوين على سبيل منع الخلو (مفتوحة) لتعادل خفة الفتحة ثقل الواو والضمة",
     "en": "(and a nūn), in compensation for the vowel or the tanwīn, by way of the exclusion of neither being absent (manʿ al-khulūw), (with a fatḥa), so that the lightness of the fatḥa may balance the heaviness of the wāw and the ḍamma,"},
    {"type": "matn",
     "ar": "(ليدل) ذلك اللحوق أو اللاحق فقط أو مع الملحوق (على أن معه) أي: مع مفرده الواحد من حيث معناه (أكثر منه)",
     "en": "(to indicate), that attachment, or the attached alone, or together with what it is attached to, (that with it), that is, with its single singular in respect of its meaning, (there is more than it);"},
    {"type": "matn",
     "ar": "ولم يقل: «من جنسه» اكتفاء بما ذكره في التثنية.",
     "en": "he did not say “of its kind”, being content with what he mentioned in the dual."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إشارة إلى ضعفه، أو كونه بحسب الاستعمال دون الوضع، لا بد له من شاهد.",
     "en": "An indication of its weakness; or [that] its being by usage rather than by coinage requires evidence."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فيه أنه مخالف لما تقرر عندهم من أن ما يفرق بينه وبين واحده بالتاء، فهو اسم جنس.",
     "en": "Against which: it conflicts with what is established among them, that whatever is distinguished from its unit by the tāʾ is a generic noun."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: المذكر مفرده بقرينة السابق.",
     "en": "That is, [for] what has a masculine singular, by the indication of what precedes."},
    {"type": "pair",
     "ar": "وفيه تنبيه على أنه كما يقال بالإضافة يقال بالوصف أيضا،",
     "en": "In it there is a pointer that, just as it is said with annexation, it is also said with qualification;"},
    {"type": "pair",
     "ar": "ولم يفسر قوله: فالمذكر بجمع المذكر الصحيح لاحتياجه إلى كثرة الحذف، أعني: المضاف والصفة",
     "en": "he did not gloss his words “so the masculine” as “the sound masculine plural”, because that would need much ellipsis, namely of the annexed term and the adjective;"},
    {"type": "pair",
     "ar": "ولا بالمذكر المجموع صحيحا؛ لأن سوق الكلام في بيان المجموع لا في بيان المذكر المجموع.",
     "en": "nor as “the masculine pluralized soundly”, because the discourse is directed at explaining the plural, not at explaining the pluralized masculine."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لفظا نحو: مسلمون أو تقديرا نحو: مصطفون، وكذا الحال في مكسور ما قبلها.",
     "en": "In wording, as in “muslimūn”, or by supposition, as in “muṣṭafawn”; and the same holds for “preceded by a kasra”."},
]
