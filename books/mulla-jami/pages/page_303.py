# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 303 (printed ٣٠٢)."""

PAGE_NUMBER = 303
PRINTED_PAGE = "٣٠٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «لأن الجر ليس علامة لذات المضاف» from the foot of PDF p. 302.
    {"type": "matn",
     "ar": "إليه، بل لحيثية كونه مضافا إليه[[١]]،",
     "en": "…ilayhi, but of the respect in which it is a muḍāf ilayhi."},
    {"type": "matn",
     "ar": "والمضاف إليه وإن كان مختصا بما عرفه به، لكن المشتمل على علامته أعم منه[[٢]]، ومما هو مشبه به،",
     "en": "Although the muḍāf ilayhi is restricted to what he defined it by, that which contains its sign is more general than it and than what resembles it;"},
    {"type": "matn",
     "ar": "فيدخل في تعريف المجرور مثل: «بحسبك درهم، وكفى بالله»، وكذا المضاف إليه بالإضافة اللفظية، وإن لم يكن داخلا في تعريفه.",
     "en": "so there enter into the definition of the genitive such as “bi-ḥasbika dirhamun” (a dirham suffices you) and “kafā bi-llāhi” (Allah suffices), and likewise the muḍāf ilayhi in verbal annexation (al-iḍāfa al-lafẓiyya), even though it does not enter into its definition."},
    {"type": "matn",
     "ar": "(والمضاف إليه) وهو ههنا غير ما هو المصطلح المشهور بينهم،",
     "en": "(And the muḍāf ilayhi): here it is other than the well-known technical term among them."},
    {"type": "matn",
     "ar": "وذهب المصنف في ذلك إلى مذهب سيبويه[[٣]] حيث أطلق المضاف إليه[[٤]] على المنسوب إليه بحرف الجر لفظا أيضا.",
     "en": "In this the author followed the doctrine of Sībawayh, who applied “muḍāf ilayhi” also to that to which something is related by an overt preposition (ḥarf al-jarr)."},
    {"type": "matn",
     "ar": "(كل اسم) حقيقة أو حكما، ليشمل الجمل التي يضاف إليها نحو: ﴿يوم ينفع الصادقين صدقهم﴾[[٥]]، فإنها في حكم المصادر.",
     "en": "(is every noun), in reality or by assimilation, so as to include the sentences to which [a noun] is annexed, as in “the day on which their truthfulness will benefit the truthful” (yawmu yanfaʿu l-ṣādiqīna ṣidquhum), for they have the status of verbal nouns (maṣādir)."},
    {"type": "matn",
     "ar": "(نسب إليه شيء) اسما كان نحو: «غلام زيد» أو فعلا مثل: «مررت بزيد».",
     "en": "(to which something is related), whether a noun, as in “ghulāmu Zaydin” (Zayd’s slave), or a verb, as in “marartu bi-Zaydin” (I passed by Zayd),"},
    {"type": "matn",
     "ar": "(بواسطة حرف الجر لفظا أو تقديرا) أي: ملفوظا كان[[٦]] ذلك الحرف كما في مثل: «مررت بزيد»، أو مقدرا",
     "en": "(by means of a preposition, overtly or by supposition), that is, whether that particle is pronounced, as in “marartu bi-Zaydin,” or supposed,"},
    {"type": "matn",
     "ar": "حال كون ذلك المقدر (مرادا) من حيث العمل بإبقاء أثره -وهو الجر[[٧]]- مثل: «غلام زيد، وخاتم فضة، وضرب اليوم»، بخلاف «قمت",
     "en": "the supposed particle being (intended) with respect to governing, by its effect, namely the genitive, being retained, as in “ghulāmu Zaydin,” “khātamu fiḍḍatin” (a ring of silver) and “ḍarbu l-yawmi” (today’s beating), unlike “qumtu…”"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "كما مر في بيان أقسام الإعراب.",
     "en": "As has passed in the account of the divisions of inflection."},
    # REVIEW: print reads «حجر سابقه»; the sense is unclear (perhaps «في حجر سابقه» or «جزء سابقه» is meant); transcribed as printed.
    {"type": "pair",
     "ar": "وإنما لم يقل بدل قوله على علم المضاف إليه على علم الإضافة؛ لأنه قصد أن يأخذ لاحق كلامه، أعني: قوله: والمضاف إليه كل اسم إلى آخره، حجر سابقه مع أن المراد متبين.",
     "en": "He did not say “the sign of annexation” in place of his words “the sign of the muḍāf ilayhi” only because he meant the later part of his statement, namely his words “and the muḍāf ilayhi is every noun…,” to be taken as [explaining] what precedes it, the intended sense being clear."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لجواز أن يتحقق علامة الشيء بدون ذلك الشيء.",
     "en": "Since the sign of a thing may be present without that thing."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وكأنه اختاره ليصح قولهم: والجر علم المضاف إليه بقدر الإمكان بلا تكلف.",
     "en": "It seems he chose it so that their saying “the genitive is the sign of the muḍāf ilayhi” would hold as far as possible without strain."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أتى الظاهر موضع الضمير للتنصيص على المراد،",
     "en": "He put the explicit noun in place of the pronoun to state the intended sense expressly,"},
    {"type": "pair",
     "ar": "ولاحتمال أنه أراد بالمضاف إليه هنا غير المضاف إليه المذكور أولا بأن يكون أعم من المضاف إليه حقيقة، ومما يشبهه نحو: كفى بالله",
     "en": "and because he may have meant by muḍāf ilayhi here something other than the muḍāf ilayhi mentioned first, namely that it be more general than the muḍāf ilayhi in the proper sense and than what resembles it, as in “kafā bi-llāhi,”"},
    {"type": "pair",
     "ar": "بخلاف المضاف إليه المذكور هنا، فإنه يختص بالمضاف إليه حقيقة.",
     "en": "unlike the muḍāf ilayhi mentioned here, for it is restricted to the muḍāf ilayhi in the proper sense."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "سورة المائدة: ١١٩.",
     "en": "Qurʾān, Sūrat al-Māʾida 5:119."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أشار به إلى أن قوله: «لفظا» خبر لـ«كان» المقدر.",
     "en": "By this he indicated that his word “lafẓan” (overtly) is the predicate of an implied “kāna.”"},
    {"type": "pair",
     "ar": "وجاز تقدير «كان» قياسا فيما كثر وقوعه. ولا خفاء في كثرة وقوع اللفظ، والتقدير في تراكيبهم،",
     "en": "Supposing “kāna” is permissible by analogy (qiyās) in what occurs frequently, and there is no doubt that the overt and the supposed occur frequently in their constructions."},
    {"type": "pair",
     "ar": "وجاز أن يكون حالا من حرف جر لاختصاصه بالإضافة. والعامل ما في الواسطة من معنى التوسط والتوسل.",
     "en": "It may also be a circumstantial accusative (ḥāl) of “ḥarf jarr,” since that is made specific by annexation; and the governor is the sense of mediation and instrumentality contained in “wāsiṭa” (means)."},
    {"type": "pair",
     "ar": "وفيه أن المصدر لا يقع حالا إلا سماعا.",
     "en": "Against this [it is said] that a verbal noun does not occur as a ḥāl except by attested usage (samāʿ)."},
    {"type": "pair",
     "ar": "وأجاز المبرد قياسا إذا كان المصدر من أقسام مدلول العامل نحو: أتانا رجلة سرعة وبطأ.",
     "en": "Al-Mubarrad allowed it by analogy when the verbal noun is one of the kinds of what the governor signifies, as in “atānā rajlatan surʿatan wa-buṭʾan.”"},
    # REVIEW: the example reads «أتانا رجلة سرعة وبطأ» as printed (the usual example is «أتانا رجلة/سرعة» etc.); transcribed as printed.
    {"type": "pair",
     "ar": "والقول بأن اللفظي والتقديري من أقسام التوسط لا يخلو عن تمحل.",
     "en": "The claim that the overt and the supposed are kinds of mediation is not free of strain (tamaḥḥul)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "بيان للواقع لا أن الأثر ملحوظ بهذا العنوان حتى يتجه ما قيل من أن تعريف المجرورات يصير دوريا؛",
     "en": "This is a statement of fact, not that the effect is considered under this title, such that the objection would hold that the definition of the genitives becomes circular;"},
    {"type": "pair",
     "ar": "لأن الخفاء في المجرور باعتبار الجر، فلو أخذ في تعريفه ما يتوقف عن الجر لزم الدور.",
     "en": "since the obscurity in the genitive concerns the genitive case, so if what depends on the genitive were taken into its definition, circularity would follow."},
    # REVIEW: print reads «يتوقف عن الجر»; «يتوقف على الجر» is the expected construction; transcribed as printed.
]
