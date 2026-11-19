# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 450 (printed ٤٤٩)."""

PAGE_NUMBER = 450
PRINTED_PAGE = "٤٤٩"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # PDF p. 449 ends with a complete sentence («… ألف وتاء»); this page opens a new one.
    # REVIEW: a small stray mark (a circle-like dot) is printed between «الصحيح» and marker [١]; ignored.
    {"type": "matn",
     "ar": "(وشرطه) أي: شرط الجمع الصحيح[[١]] المؤنث (إن كان) مفرده (صفة، وله) أي: ولذلك المفرد (مذكر فأن يكون[[٢]] مذكره) أي: مذكر ذلك المفرد (جمع بالواو والنون) لئلا يلزم[[٣]] مزية الفرع على الأصل",
     "en": "(And its condition), that is, the condition of the sound feminine plural, (if) its singular (is an adjective and it has), that is, that singular has, (a masculine, is that its masculine), that is, the masculine of that singular, (be pluralized with the wāw and the nūn), lest the branch be given an advantage over the root."},
    {"type": "matn",
     "ar": "(وإن لم يكن له) أي: لمفرده (مذكر) جمع بالواو والنون (فألا يكون) أي: فشرط صحة جمعيته ألا يكون (مجردا) عن تاء التأنيث (كـ«حائض»)؛",
     "en": "(And if it does not have), that is, if its singular does not have, (a masculine) pluralized with the wāw and the nūn, (then that it not be), that is, the condition for its validly taking this plural is that it not be, (bare) of the feminine tāʾ, (like “ḥāʾiḍ”) (menstruating);"},
    {"type": "matn",
     "ar": "لأنه يقال في جمع حائضة: «حائضات»، فلو قيل في جمع حائض أيضا: «حائضات» لزم الالتباس.",
     "en": "for one says “ḥāʾiḍāt” in the plural of “ḥāʾiḍa”, so if one also said “ḥāʾiḍāt” in the plural of “ḥāʾiḍ”, confusion would follow."},
    {"type": "matn",
     "ar": "(وإلا) عطف على قوله: «إن كان صفة»، أي: وإن لم يكن المؤنث صفة، بل كان اسما (جمع) هذا الجمع (مطلقا) أي: من غير اعتبار شرط، مثل: «طلحات وزينبات» في جمع «طلحة وزينب».",
     "en": "(Otherwise), coordinated with his words “if it is an adjective”, that is, if the feminine is not an adjective but is a substantive, (it is pluralized) with this plural (without restriction), that is, without regard to any condition, as in “Ṭalḥāt” and “Zaynabāt” in the plural of “Ṭalḥa” and “Zaynab”."},
    {"type": "matn",
     "ar": "وفي شرح الرضي: أن هذا الإطلاق ليس بسديد؛ لأن الأسماء المؤنثة بتاء مقدرة كـ«نار وشمس» ونحوهما من الأسماء التي تأنيثها غير حقيقي لا يطرد فيها الجمع بالألف والتاء،",
     "en": "In the commentary of al-Raḍī [it is stated] that this unrestricted statement is not sound; for in nouns feminine by an implied tāʾ, like “nār” (fire) and “shams” (sun), and similar nouns whose femininity is not real, the plural with the alif and the tāʾ is not regular;"},
    {"type": "matn",
     "ar": "بل هو فيها مسموع كـ«السماوات والكائنات»، وذلك لخفاء هذا التأنيث؛ لأنه ليس بحقيقي، ولا ظاهر العلامة.",
     "en": "rather, in them it is known only by attestation (samāʿ), as in “al-samāwāt” (the heavens) and “al-kāʾināt” (existing things); this is because of the obscurity of this femininity, since it is neither real nor marked by a visible sign."},

    {"type": "section", "ar": "[جمع التكسير]",
     "en": "The Broken Plural (Jamʿ al-Taksīr)"},

    {"type": "matn",
     "ar": "(جمع التكسير: ما تغير) أي: جمع تغير (بناء واحده) من حيث نفسه وأموره الداخلة فيه -كما هو المتبادر[[٤]]- فلا ينتقض بجمع السلامة، لتغير بناء واحده بلحوق الحروف الخارجة الزائدة به.",
     "en": "(The broken plural is that in which is changed), that is, a plural in which is changed, (the form of its singular), with respect to the form itself and the matters internal to it, as is the immediately understood sense; so it is not undermined by the sound plural, [where] the form of its singular is changed by the attachment of extraneous added letters to it."},
    {"type": "matn",
     "ar": "وأيضا المتبادر من تغيره تغير يكون لحصول الجمعية، فلا ينتقض أيضا بمثل: «مصطفون»، فإن تغير الواحد فيه يلزم بعد حصول الجمعية.",
     "en": "Further, what is immediately understood from its change is a change that takes place to bring about plurality; so it is also not undermined by the like of “muṣṭafawn”, for the change of the singular in it follows after plurality has been brought about."},
    {"type": "matn",
     "ar": "وأما التغير المذكور في تعريف الجمع مطلقا، فهو أعم من أن يكون من حيث ذات",
     "en": "As for the change mentioned in the definition of the plural in general, it is more general than that it be with respect to the essence…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "جرى في إرجاع ضمير «وشرطه» ههنا على الظاهر لعدم الصارف بخلاف ما تقدم.",
     "en": "In referring the pronoun of “wa-sharṭuhu” here he has followed the apparent sense, there being nothing to divert it, unlike what preceded."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فهو أن يكون، الضمير راجع إلى المبتدأ الذي هو «وشرطه».",
     "en": "[That is:] “then it is that it be”; the pronoun refers back to the subject (mubtadaʾ), which is “wa-sharṭuhu”."},
    {"type": "pair",
     "ar": "والشرط مع الجزاء في محل الرفع خبر المبتدأ، كذا في الرضي.",
     "en": "The condition together with its apodosis is in the position of the nominative, as the predicate (khabar) of the subject; so in al-Raḍī."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "أي: لو جمع المؤنث جمع السلامة ولم يجمع مذكره، وكذلك يلزم مزية الفرع على الأصل.",
     "en": "That is, if the feminine were given the sound plural and its masculine were not, then likewise the branch would be given an advantage over the root."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: أن المتبادر من نسبة التغير إلى البناء أن يكون التغير في ذاته وباعتبار أجزائه لا التغير العارض له باعتبار أمر خارج عنه سواء كان التغير حقيقيا أو اعتباريا،",
     "en": "He means that what is immediately understood from ascribing the change to the form is that the change be in the form itself and with respect to its parts, not a change occurring to it with respect to something external to it, whether the change be real or notional;"},
    {"type": "pair",
     "ar": "وليس مراده أن المتبادر من التغير التغير في ذاته حتى يرد عليه أنه كما أن المتبادر من التغير ذلك المتبادر منه أن يكون حقيقيا،",
     "en": "his meaning is not that what is immediately understood from “change” is change in the thing itself, so that the objection would be raised against him that, just as that is what is immediately understood from “change”, so too what is immediately understood from it is that it be real;"},
    {"type": "pair",
     "ar": "فحمل التغير على المتبادر باعتبار، وعلى غير المتبادر باعتبار تكلف.",
     "en": "so to take “change” in the immediately understood sense in one respect and in a sense not immediately understood in another respect would be contrived."},
]
