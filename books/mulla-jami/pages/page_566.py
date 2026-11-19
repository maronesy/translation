# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 566 (printed ٥٦٥)."""

PAGE_NUMBER = 566
PRINTED_PAGE = "٥٦٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues the discussion of the negative particle after lightened «أن» (PDF p. 565).
    {"type": "matn",
     "ar": "فإنه لا يحصل بمجرده الفرق بين المخففة والمصدرية، فإنه يجتمع مع كل منهما.",
     "en": "For by itself it does not produce the distinction between the lightened [an] and the infinitival [an], since it occurs together with each of them."},
    {"type": "matn",
     "ar": "فالفارق بينهما:",
     "en": "So what distinguishes them is"},
    {"type": "matn",
     "ar": "إما من حيث المعنى؛ لأنه إن عني به الاستقبال، فهي المخففة وإلا فهي المصدرية[[١]].",
     "en": "either in respect of meaning: for if the future is intended by it, it is the lightened [an]; otherwise it is the infinitival [an];"},
    {"type": "matn",
     "ar": "وإما من حيث اللفظ؛ لأنه إن كان الفعل المنفي منصوبا؛ فهي المصدرية وإلا فهي المخففة.",
     "en": "or in respect of wording: for if the negated verb is in the subjunctive (manṣūb), it is the infinitival [an]; otherwise it is the lightened [an]."},

    {"type": "section", "ar": "[كأن]",
     "en": "Kaʾanna"},

    {"type": "matn",
     "ar": "(وكأن للتشبيه) أي: لإنشائه.",
     "en": "(And kaʾanna is for likening (tashbīh)), that is, for producing a likening."},
    {"type": "matn",
     "ar": "وهي حرف برأسه على الصحيح حملا على أخواتها، ولأن الأصل عدم التركيب،",
     "en": "On the sound view it is a particle in its own right, by analogy with its sisters, and because the default is the absence of compounding."},
    {"type": "matn",
     "ar": "ومذهب الخليل[[٢]] أنها مركبة من «الكاف وإن» المكسورة، وأصل «كأن زيدا الأسد»: «إن زيدا كالأسد»،",
     "en": "The doctrine of al-Khalīl is that it is compounded of “the kāf and inna” with kasra; the origin of “kaʾanna Zaydan al-asadu” (it is as though Zayd were the lion) is “inna Zaydan ka-l-asadi” (Zayd is like the lion)."},
    {"type": "matn",
     "ar": "قدمت الكاف؛ ليعلم إنشاء التشبيه من أول الأمر، وفتحت الهمزة؛ لأن الكاف في الأصل جارة، وإن خرجت عن حكم الجارة.",
     "en": "The kāf was put first so that the producing of a likening be known from the very outset, and the hamza was given a fatḥa because the kāf is originally a genitive-governing [particle], even though it has left the status of the genitive-governing one."},
    {"type": "matn",
     "ar": "والجارة إنما تدخل على المفرد، فراعوا الصورة، وفتحوا الهمزة، وإن كان المعنى على الكسر.",
     "en": "The genitive-governing [particle] enters only upon a single word (mufrad); so they observed the outward form and gave the hamza a fatḥa, even though the meaning is that of the kasra [form]."},
    {"type": "matn",
     "ar": "(وتخفف) أي: «كأن» (فتلغى) عن العمل (على) الاستعمال (الأفصح) لخروجها عن المشابهة؛ لفوات فتحة الآخر، كقول الشاعر:",
     "en": "(And it is lightened), that is, “kaʾanna”, (and then it is cancelled) from governing, (according to the more eloquent) usage, because it has left [its] resemblance [to the verb] through the loss of the fatḥa at the end; as in the poet’s words:"},
    {"type": "verse",
     "ar": "ونحر مشرق اللون          كأن ثدياه حقان",
     "en": "“And a bosom of radiant hue, as though its two breasts (thadyāhu) were two small caskets.”"},
    {"type": "matn",
     "ar": "وإن أعملتها قلت: «كأن ثدييه»، لكنه على الاستعمال الغير الأفصح، لما عرفت.",
     "en": "If you make it govern, you say “kaʾan thadyayhi”; but that is according to the less eloquent usage, for the reason you have learned."},
    {"type": "matn",
     "ar": "وإذا لم تعملها لفظا، ففيها ضمير الشأن مقدر عندهم، كما في أن المخففة.",
     "en": "If you do not make it govern overtly, then according to them a pronoun of the matter is implied in it, as with the lightened an."},
    {"type": "matn",
     "ar": "ويجوز أن يقال[[٣]]: غير مقدر بعدها الضمير، لعدم الداعي إليه، كما كان في أن المخففة.",
     "en": "It may also be said that no pronoun is implied after it, since there is nothing calling for it, as was the case with the lightened an."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هكذا في النسخ رأيناها، والصواب إن عني به الاستقبال، فهي المصدرية، وإلا فهي المخففة؛",
     "en": "This is how it stands in the copies we have seen; the correct reading is: if the future is intended by it, it is the infinitival [an], otherwise it is the lightened [an];"},
    {"type": "pair",
     "ar": "لأن المصدرية تخلص المضارع للاستقبال دون المخففة.",
     "en": "because the infinitival [an] restricts the imperfect (muḍāriʿ) to the future, whereas the lightened one does not."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فهي عنده للتشبيه والتأكيد.",
     "en": "So on his view it serves for likening and for emphasis."},
    {"type": "pair",
     "ar": "في المغني: أنه مذهب الأكثر حتى قيل: إنه كالمجمع عليه.",
     "en": "In al-Mughnī [it is stated] that this is the doctrine of the majority, so much so that it has been said to be virtually agreed upon."},

    # ---------------- Footnote 3 (runs on to PDF p. 567) ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وهو الموافق لعبارة المتن هنا حيث قال ههنا: وتخفف فتعمل في ضمير شأن مقدر، وهنا وتخفف فتلغي على الأفصح،",
     "en": "This agrees with the wording of the base text (matn) here, since he said here [of anna]: “and it is lightened and then governs an implied pronoun of the matter”, and here [of kaʾanna]: “and it is lightened and then is cancelled, according to the more eloquent [usage]”;"},
    {"type": "pair",
     "ar": "ولعبارته في بحث ضمير الشأن حيث قال: وحذفه منصوبا ضعيف إلا مع أن إذا",
     "en": "and with his wording in the discussion of the pronoun of the matter, where he said: “Its omission when in the accusative is weak, except with an when…"},
]
