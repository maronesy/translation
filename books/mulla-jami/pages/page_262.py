# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 262 (printed ٢٦١)."""

PAGE_NUMBER = 262
PRINTED_PAGE = "٢٦١"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 261 ends with a complete sentence («فلا بد من الواو على الصحيح.»).
    {"type": "matn",
     "ar": "(والمضارع المثبت[[١]]) أي: الجملة الفعلية التي يكون الفعل فيها مضارعا مثبتا متلبسة: (بالضمير[[٢]] وحده)",
     "en": "(The affirmative imperfect), that is, the verbal clause whose verb is an affirmative imperfect, is joined (by the pronoun alone),"},
    {"type": "matn",
     "ar": "لمشابهته لفظا ومعنى لاسم الفاعل المستغني عن الواو نحو: «جاءني زيد يسرع».",
     "en": "because of its resemblance in form and meaning to the active participle, which has no need of the wāw, as in “Zayd came to me hurrying.”"},
    {"type": "matn",
     "ar": "(وما سواهما) أي: ما سوى الجملة الاسمية والفعلية المشتملة على المضارع المثبت من الجمل المشتملة على المضارع المنفي[[٣]] أو الماضي المثبت أو المنفي",
     "en": "(What is other than these two), that is, other than the nominal clause and the verbal clause containing an affirmative imperfect, namely the clauses containing a negated imperfect, or an affirmative or negated perfect, [is joined]"},
    {"type": "matn",
     "ar": "(بالواو والضمير معا أو بأحدهما) وحده من غير ضعف عند الاكتفاء بالضمير، لعدم قوة استقلالها كالاسمية.",
     "en": "(by the wāw and the pronoun together, or by one of them) alone, without weakness when the pronoun alone suffices, because they lack the strong self-sufficiency of the nominal clause."},
    {"type": "matn",
     "ar": "فالمضارع المنفي نحو: «جاءني زيد وما يتكلم غلامه»، أو «جاءني زيد ما يتكلم غلامه»، أو «جاءني زيد وما يتكلم عمرو».",
     "en": "The negated imperfect: “Zayd came to me and his servant was not speaking,” or “Zayd came to me, his servant not speaking,” or “Zayd came to me and ʿAmr was not speaking.”"},
    {"type": "matn",
     "ar": "والماضي المثبت نحو: «جاءني زيد وقد خرج غلامه»، أو «جاءني زيد قد خرج غلامه»، أو «جاءني زيد وقد خرج عمرو».",
     "en": "The affirmative perfect: “Zayd came to me and his servant had gone out,” or “Zayd came to me, his servant having gone out,” or “Zayd came to me and ʿAmr had gone out.”"},
    {"type": "matn",
     "ar": "والماضي المنفي نحو: «جاءني زيد وما خرج غلامه»، أو «جاءني زيد ما خرج غلامه»، أو «جاءني زيد وما خرج عمرو».",
     "en": "The negated perfect: “Zayd came to me and his servant had not gone out,” or “Zayd came to me, his servant not having gone out,” or “Zayd came to me and ʿAmr had not gone out.”"},
    {"type": "matn",
     "ar": "(ولا بد في الماضي المثبت) لا المنفي (من) دخول لفظة («قد») المقربة زمان الماضي إلى الحال لغة على الماضي المثبت الواقع حالا،",
     "en": "(In the affirmative perfect), not the negated, (there must be) the entry of the word (“qad”), which brings the time of the perfect near to the present (ḥāl in the lexical sense), on the affirmative perfect occurring as a ḥāl,"},
    {"type": "matn",
     "ar": "ليدل[[٤]] بها على قرب زمانه إلى زمان صدور الفعل من ذي الحال أو وقوعه عليه تجوزا؛",
     "en": "so that it may indicate, figuratively, the nearness of its time to the time of the action’s issuing from the dhū al-ḥāl or falling upon it;"},
    {"type": "matn",
     "ar": "لأن المتبادر من الماضي المثبت إذا وقع حالا أن مضيه إنما هو بالنسبة إلى زمان العامل، فلا بد من «قد» حتى تقربه إليه، فيقاربه،",
     "en": "for what first comes to mind from an affirmative perfect occurring as a ḥāl is that its pastness is relative to the time of the governor; so “qad” is needed to bring it near to that, so that it is close to it."},
    {"type": "matn",
     "ar": "وهذا بخلاف مذهب الكوفيين، فإنهم لا يوجبون «قد» ظاهرة ولا مقدرة",
     "en": "This is contrary to the doctrine of the Kufans, for they do not require “qad,” whether overt or understood;"},
    {"type": "matn",
     "ar": "سواء كانت (ظاهرة) في اللفظ نحو: «جاءني زيد قد ركب غلامه»",
     "en": "whether it is (overt) in the wording, as in “Zayd came to me, his servant having ridden,”…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "والحال المؤكدة مثله كما عرفت.",
     "en": "The corroborative ḥāl is like it, as you have learned."},
    {"type": "pair",
     "ar": "وكذا المضارع المنفي بكلمة ما، والمضارع المنفي بكلمة لم وبكلمة لا في الأغلب.",
     "en": "So too, mostly, the imperfect negated by “mā,” and the imperfect negated by “lam” and by “lā.”"},
    {"type": "pair",
     "ar": "ويشترط في المضارع المثبت الواقع حالا خلوه عن حرف الاستقبال كالسين وسوف ولن.",
     "en": "It is a condition for the affirmative imperfect occurring as a ḥāl that it be free of a particle of futurity such as sa-, sawfa and lan."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "قد سمع بالواو.",
     "en": "It has been heard with the wāw."},
    {"type": "pair",
     "ar": "وذلك لأنها جملة وإن شابهت المفرد، أو لأنه خبر مبتدأ محذوف.",
     "en": "That is because it is a clause, even though it resembles a single word; or because it is the predicate of an elided mubtadaʾ."},
    {"type": "pair",
     "ar": "ويشترط في المضارع الواقع حالا خلوه عن حرف الاستقبال كالسين ولن ونحوهما.",
     "en": "It is a condition for the imperfect occurring as a ḥāl that it be free of a particle of futurity such as sa- and lan and the like."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وإن كان بـ«لم» خلافا للأندلسي فإنه قال: لا بد فيه من الواو وإن كان مع الضمير.",
     "en": "Even if [negated] by “lam,” contrary to al-Andalusī, who said: it must have the wāw, even with the pronoun."},
    # REVIEW: print reads «انتهى» twice (sense requires «انتفى», "is negated"); transcribed as printed.
    {"type": "pair",
     "ar": "قال الشيخ الرضي: إذا انتهى المضارع بلفظة \"ما\" لم يدخله الواو.",
     "en": "Shaykh al-Raḍī said: when the imperfect is negated by the word “mā,” the wāw does not enter it."},
    {"type": "pair",
     "ar": "وإذا انتهى المضارع بـ\"لا\" لزمه الضمير. والأغلب تجرده عن الواو.",
     "en": "When the imperfect is negated by “lā,” the pronoun is required, and it is mostly without the wāw."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "هذا تحقيق ذكره السيد الشريف قدس سره.",
     "en": "This is an exact analysis given by al-Sayyid al-Sharīf, may his secret be sanctified."},
]
