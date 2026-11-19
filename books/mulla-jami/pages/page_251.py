# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 251 (printed ٢٥٠)."""

PAGE_NUMBER = 251
PRINTED_PAGE = "٢٥٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «نحو: ﴿بل ملة إبراهيم حنيفا﴾،» from the foot of PDF p. 250.
    {"type": "matn",
     "ar": "و﴿أن يأكل لحم أخيه ميتا﴾[[١]] فإنه يصح أن تقول: «بل نتبع إبراهيم» مقام «بل نتبع ملة إبراهيم»، «أن يأكل أخاه» مقام «أن يأكل لحم أخيه»،",
     "en": "…and “that he should eat the flesh of his brother dead”; for it is valid to say “Nay, we follow Abraham” in place of “Nay, we follow the creed of Abraham,” and “that he should eat his brother” in place of “that he should eat the flesh of his brother”;"},
    {"type": "matn",
     "ar": "أو كان المضاف فاعلا أو مفعولا، وهو جزء المضاف إليه، فكان الحال عن المضاف إليه[[٢]] هو الحال عن المضاف، وإن لم يصح قيامه مقامه،",
     "en": "or when the muḍāf is an agent or an object and is a part of the muḍāf ilayhi, so that the ḥāl of the muḍāf ilayhi is the ḥāl of the muḍāf, even if it is not valid for it to stand in its place,"},
    {"type": "matn",
     "ar": "كما في قوله تعالى: ﴿أن دابر هؤلاء مقطوع مصبحين﴾[[٣]]،",
     "en": "as in His words, the Exalted: “that the last remnant of these would be cut off by morning”;"},
    {"type": "matn",
     "ar": "فقوله: «مصبحين» حال من «هؤلاء» باعتبار أن الدابر المضاف إليه جزؤه؛ فإن دابر الشيء أصله،",
     "en": "for His word “muṣbiḥīn” (at morning) is a ḥāl of “these” by consideration of the fact that “the remnant” (al-dābir), which is annexed to it, is a part of it—for the dābir of a thing is its root;"},
    {"type": "matn",
     "ar": "و«الدابر» مفعول ما لم يسم فاعله باعتبار الضمير المستكن في المقطوع، فكأنه حال عن مفعول ما لم يسم فاعله.",
     "en": "and “al-dābir” is the object of a verb whose agent is not named (mafʿūl mā lam yusamma fāʿiluhu) by consideration of the pronoun latent in “maqṭūʿ”; so it is as though it were a ḥāl of the object of a verb whose agent is not named."},
    {"type": "matn",
     "ar": "ولو قرئ[[٤]]: «تبين» على صيغة الماضي المعلوم من باب التفعل، أو «يبين» على صيغة المضارع المجهول[[٥]] من باب التفعيل،",
     "en": "If [the definition] were read “tabayyana,” in the form of the active past tense of the tafaʿʿul pattern, or “yubayyanu,” in the form of the passive imperfect of the tafʿīl pattern,"},
    {"type": "matn",
     "ar": "وجعل الجار والمجرور متعلقا به لا بالمفعول دخل فيه الحال من المفعول معه أو المفعول المطلق من غير حاجة إلى تعميم الفاعل أو المفعول[[٦]] إلا لدخول ما وقع حالا عن المضاف إليه.",
     "en": "and the preposition and its object were made dependent on it rather than on “the object,” then the ḥāl of the concomitant object or of the absolute object would enter into it without any need to generalize “agent” or “object,” except to include what occurs as a ḥāl of the muḍāf ilayhi."},
    {"type": "matn",
     "ar": "(مثل: «ضربت زيدا قائما») مثال اللفظي الملفوظ حقيقة،",
     "en": "(Such as “I struck Zayd standing”): an example of the verbal [kind] actually uttered;"},
    {"type": "matn",
     "ar": "فإن فاعلية «تاء المتكلم» ومفعولية «زيد» إنما هي باعتبار لفظ هذا الكلام ومنطوقه من غير اعتبار معنى خارج عنه، وهما ملفوظان حقيقة.",
     "en": "for the agency of the first-person “tāʾ” and the objecthood of “Zayd” are only by consideration of the wording of this speech and its explicit expression, without regard to a meaning outside it, and both are actually uttered."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سورة الحجرات: ١٢.",
     "en": "Qurʾān, Sūrat al-Ḥujurāt 49:12."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأن الداخل في الذات في حكم الذات.",
     "en": "Because what is included in an entity has the status of that entity."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة الحجر: ٦٦.",
     "en": "Qurʾān, Sūrat al-Ḥijr 15:66."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "هذا موافق لما قاله بعضهم من جواز الحال عن المفعول معه وعن المصدر بلا تأويل.",
     "en": "This agrees with what some have said: that a ḥāl of the concomitant object and of the maṣdar is permitted without reinterpretation (taʾwīl)."},
    {"type": "pair",
     "ar": "والجمهور جوزوا الحال عنهما لتأويلهما بالفاعل أو المفعول به.",
     "en": "The majority permitted a ḥāl of them because they are reinterpreted as the agent or the direct object."},
    {"type": "pair",
     "ar": "ولا يخفى أنه لو قرئ كذلك لزم جواز الحال عن المفعول فيه.",
     "en": "It is not hidden that if it were read so, it would follow that a ḥāl of the adverbial object (mafʿūl fīhi) is permitted."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أو على صيغة المضارع المعلوم المخاطب، وهو أوفق بما هو المشهور.",
     "en": "Or in the form of the active imperfect, second person [tubayyinu]; and this is more in keeping with what is well known."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا يخفى أن المتبادر من غير حاجة إلى تعميم الفاعل أو المفعول لدخول أحد الحالين،",
     "en": "It is not hidden that what first comes to mind from “without any need to generalize ‘agent’ or ‘object’” is [that there is no need] for including either of the two ḥāls;"},
    {"type": "pair",
     "ar": "فحينئذ لا يصح استثناء قوله: إلا لدخول ما وقع حالا عن المضاف إليه عنه.",
     "en": "in that case, the exception in his words “except to include what occurs as a ḥāl of the muḍāf ilayhi” cannot validly be made from it."},
    {"type": "pair",
     "ar": "واعلم أن قراءة عبارة المتن على أحد هذين الوجهين إنما يصح إذا تحقق أن مذهب النحاة أن الحال يقع عن المفعول مطلقا، ولا تتقيد بالمفعول به محققا أو مؤولا",
     "en": "Know that reading the wording of the matn in either of these two ways is valid only if it is established that the doctrine of the grammarians is that the ḥāl occurs of the object without restriction, and is not confined to the direct object, actual or by reinterpretation,"},
    {"type": "pair",
     "ar": "بجعل العرب الحال في «ضربت الضرب شديدا» عن الضرب بلا تأويل بإحداث الضرب.",
     "en": "by the Arabs’ making the ḥāl in “I struck the striking severe” a ḥāl of “the striking” without reinterpreting it as “producing the striking.”"},
]
