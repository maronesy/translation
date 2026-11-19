# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 105 (printed ١٠٤)."""

PAGE_NUMBER = 105
PRINTED_PAGE = "١٠٤"   # Arabic-Indic, as printed

BLOCKS = [
    {"type": "matn",
     "ar": "تكون حاصلة في ضمنه[[١]] على أن تكون الياء للنسبة.",
     "en": "[the definiteness] being realized within it — on the assumption that the yāʾ is that of relative attribution (nisba)."},
    {"type": "matn",
     "ar": "وإنما جعلت مشروطة بالعلمية؛ لأن تعريف المضمرات والمبهمات لا يوجد إلا في المبنيات، ومنع الصرف من أحكام المعربات، والتعريف باللام أو الإضافة يجعل غير المنصرف منصرفا[[٢]]،",
     "en": "It was made conditional upon proper-nounhood (ʿalamiyya) only because the definiteness of the pronouns (muḍmarāt) and the vague nouns (mubhamāt) occurs solely in indeclinable words (mabniyyāt), whereas triptote-prevention (manʿ al-ṣarf) is among the rulings of declinable words (muʿrabāt); and definiteness by the article or by annexation makes the diptote (ghayr al-munṣarif) into a triptote (munṣarif),"},
    {"type": "matn",
     "ar": "أو في حكم المنصرف كما سيجيء، فلا يتصور كونه سببا لمنع الصرف، فلم يبق إلا التعريف العلمي[[٣]].",
     "en": "or into the ruling of the triptote, as will come; so it cannot be conceived to be a cause for triptote-prevention. Thus there remains only definiteness through proper-nounhood."},
    {"type": "matn",
     "ar": "وإنما جعل المعرفة سببا، والعلمية شرطها، ولم يجعل العلمية سببا، كما جعل البعض[[٤]]؛ لأن فرعية التعريف للتنكير أظهر[[٥]] من فرعية العلمية له.",
     "en": "Definiteness (maʿrifa) was made the cause and proper-nounhood its condition, and proper-nounhood was not made the cause — as some did — because the subordination (farʿiyya) of definiteness to indefiniteness is more evident than the subordination of proper-nounhood to it."},

    {"type": "section", "ar": "[ العجمة ]",
     "en": "Foreign Origin (al-ʿUjma)"},

    {"type": "matn",
     "ar": "(العجمة) وهي: كون اللفظ مما وضعه غير العرب[[٦]]، ولتأثيرها في منع الصرف شرطان:",
     "en": "Foreign origin (al-ʿujma): it is that the word is of what was coined by non-Arabs; and for its being effective in preventing full inflection there are two conditions:"},
    {"type": "matn",
     "ar": "١-(شرطها) الأول: (أن تكون علمية) أي: منسوبة إلى العلم (في) اللغة (العجمية) بأن يكون متحققة في ضمن العلم في العجم حقيقة كـ«إبراهيم» أو حكما بأن ينقله العرب من لغة العجم إلى العلمية من غير تصرف فيه قبل النقل كـ«قالون»،",
     "en": "1 — Its first condition: that it be [attached to] proper-nounhood — that is, related to a proper name — in the non-Arab (ʿajamī) language; whether by its being actually realized within a proper name among the non-Arabs, as in “Ibrāhīm,” or by supposition (ḥukman), in that the Arabs transferred it from the non-Arab language into proper-name status without any modification of it before the transfer, as in “Qālūn” —"},
    {"type": "matn",
     "ar": "فإنه كان في العجم اسم جنس[[٧]]، سمي به أحد رواة القراء[[٨]]، لجودة قراءته، قبل أن يتصرف فيه العرب، فكأنه كان علما في العجمية.",
     "en": "for among the non-Arabs it was a generic noun (ism jins), by which one of the transmitters of the Qurʾānic readings was named — on account of the excellence of his recitation — before the Arabs modified it; so it is as though it had been a proper name in the non-Arab tongue."},

    {"type": "rule"},

    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الأولى فيه «فيه». الأظهر أن يقال: حاصلة فيه حصول الصفة في موصوفها.",
     "en": "The better wording here is “in it” (fīhi). The more evident formulation is to say: realized within it in the way an attribute is realized in the thing it qualifies."},
    {"type": "pair",
     "ar": "ولا يخفى أن التعريف الذي شرط تأثيره بالعلمية لا تحقق له إلا تحقق العلمية بخلاف البواقي، فإن تحققها مغاير لتحقق العلمية.",
     "en": "It is not hidden that the definiteness whose effectiveness is conditioned upon proper-nounhood has no realization other than the realization of proper-nounhood — unlike the remaining [causes], for their realization is distinct from the realization of proper-nounhood."},

    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: حقيقة أو حكما. وفي بعض النسخ: يجعل غير المنصرف منصرفا، أو في حكمه، وهو ظاهر.",
     "en": "That is: really or by supposition. In some copies: “it makes the diptote a triptote, or [puts it] in its ruling,” which is plain."},
    {"type": "pair",
     "ar": "قوله: (يجعل غير المنصرف منصرفا) أو في حكم المنصرف.",
     "en": "His words “it makes the diptote a triptote” — or into the ruling of the triptote."},

    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "هذا مبني على أن السبب الآخر في «أجمع» وأخواته الصفة الأصلية أو العلمية لا التعريف بالإضافة المقدرة أو اللام المقدرة، كما ذهب إليه جمع.",
     "en": "This is built upon [the view] that the other cause in “ajmaʿ” and its sisters is the original adjectival quality or proper-nounhood, not definiteness through implied annexation or an implied article — as a group has held."},

    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: جار الله. واستغنى عن الاشتراط.",
     "en": "That is: Jār Allāh [al-Zamakhsharī]. And he dispensed with [stating] the condition."},

    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لأن الفرعية لمقابلة التنكير، والتعريف يذكر في مقابلة التنكير لا العلمية.",
     "en": "Because subordination is by way of contrasting with indefiniteness, and definiteness is mentioned as the counterpart of indefiniteness, not of proper-nounhood."},

    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا غير. وطريق معرفتها النقل، وإجماع أهل اللغة على ما نقل عن صاحب القواعد.",
     "en": "Nothing else. The means of knowing it is transmission (naql) and the consensus of the philologists, according to what has been reported from the author of al-Qawāʿid."},

    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "بمعنى الجيد في لغة الروم.",
     "en": "Meaning “the excellent one” in the language of the Byzantines (al-Rūm)."},

    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "سمي به رواية عيسى بن مينا.",
     "en": "By it was named the transmission (riwāya) of ʿĪsā ibn Mīnā."},
]
